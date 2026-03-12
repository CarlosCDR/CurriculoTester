from flask import Flask, render_template, request, flash, redirect, url_for, send_file, jsonify
import json
import os
import tempfile
from werkzeug.utils import secure_filename
from datetime import datetime
import io

# Importar classes do aplicativo desktop
from main import ProcessadorPDF, AnalisadorCurriculo, CriterioCurriculo

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
app.config['UPLOAD_FOLDER'] = app.config.get('UPLOAD_FOLDER', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Configurações
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    """Página inicial"""
    criterios = CriterioCurriculo.CRITERIOS_PREDEFINIDOS
    return render_template('index.html', criterios=criterios)

@app.route('/analisar', methods=['POST'])
def analisar():
    """Processa a análise do currículo"""
    # Verificar se arquivo foi enviado
    if 'curriculo' not in request.files:
        flash('Nenhum arquivo selecionado', 'error')
        return redirect(url_for('index'))

    file = request.files['curriculo']
    if file.filename == '':
        flash('Nenhum arquivo selecionado', 'error')
        return redirect(url_for('index'))

    if not allowed_file(file.filename):
        flash('Apenas arquivos PDF são permitidos', 'error')
        return redirect(url_for('index'))

    # Garantir que o diretório de upload existe
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    try:
        # Salvar arquivo temporariamente
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extrair texto do PDF
        texto = ProcessadorPDF.extrair_texto(filepath)

        if texto.startswith("Erro"):
            flash(f'Erro ao processar PDF: {texto}', 'error')
            return redirect(url_for('index'))

        # Obter critérios selecionados
        criterios_ativos = []
        criterios_config = CriterioCurriculo.CRITERIOS_PREDEFINIDOS

        for criterio in criterios_config.keys():
            if request.form.get(f'criterio_{criterio.replace(" ", "_").replace("ç", "c").replace("ã", "a").replace("é", "e")}'):
                criterios_ativos.append(criterio)

        if not criterios_ativos:
            criterios_ativos = list(criterios_config.keys())

        # Analisar currículo
        analisador = AnalisadorCurriculo()
        resultado = analisador.analisar(texto, criterios_ativos)

        # Limpar arquivo temporário
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
            except Exception as e:
                flash(f'Erro ao remover arquivo temporário: {str(e)}', 'error')

        # Renderizar resultado
        return render_template('resultado.html',
                             resultado=resultado,
                             criterios_ativos=criterios_ativos,
                             nome_arquivo=filename)

    except Exception as e:
        # Catch specific exception
        raise e

@app.route('/configuracao', methods=['GET', 'POST'])
def configuracao():
    """Página de configuração avançada"""
    # Define constants for file paths
    CRITERIOS_FILE = 'criterios.json'
    EXEMPLOS_FILE = 'exemplos_vagas.json'

    try:
        if not os.path.exists(CRITERIOS_FILE):
            with open(CRITERIOS_FILE, 'w', encoding='utf-8') as f:
                json.dump(CriterioCurriculo.CRITERIOS_PREDEFINIDOS, f)

        with open(CRITERIOS_FILE, 'r', encoding='utf-8') as f:
            criterios_custom = json.load(f)
    except json.JSONDecodeError as e:
        criterios_custom = CriterioCurriculo.CRITERIOS_PREDEFINIDOS
        flash(f"Erro ao carregar {CRITERIOS_FILE}: {str(e)}", 'error')

    try:
        if not os.path.exists(EXEMPLOS_FILE):
            with open(EXEMPLOS_FILE, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        with open(EXEMPLOS_FILE, 'r', encoding='utf-8') as f:
            exemplos = json.load(f)
    except json.JSONDecodeError as e:
        exemplos = {}
        flash(f"Erro ao carregar {EXEMPLOS_FILE}: {str(e)}", 'error')

    return render_template('configuracao.html', criterios=criterios_custom, exemplos=exemplos)

@app.route('/configuracoes', methods=['GET', 'POST'])
def configuracoes():
    """Página de configurações"""
    if request.method == 'POST':
        try:
            # Save settings
            new_settings = request.json
            with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
                json.dump(new_settings, f, indent=4)
            return jsonify({"message": "Configurações salvas com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Load settings
    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)

    with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
        settings = json.load(f)

    return render_template('configuracoes.html', settings=settings)

@app.route('/sobre', methods=['GET'])
def sobre():
    """Página sobre"""
    return render_template('sobre.html')

@app.route('/ajuda', methods=['GET'])
def ajuda():
    """Página de ajuda"""
    return render_template('ajuda.html')

@app.route('/api/analisar', methods=['POST'])
def api_analisar():
    """API endpoint para análise (JSON)"""
    try:
        if 'file' not in request.files:
            return {'error': 'Nenhum arquivo enviado'}, 400

        file = request.files['file']
        if not allowed_file(file.filename):
            return {'error': 'Apenas arquivos PDF são permitidos'}, 400

        # Salvar temporariamente
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Processar
        texto = ProcessadorPDF.extrair_texto(filepath)
        if texto.startswith("Erro"):
            return {'error': texto}, 400

        # Analisar
        criterios_ativos = request.form.getlist('criterios') or list(CriterioCurriculo.CRITERIOS_PREDEFINIDOS.keys())
        analisador = AnalisadorCurriculo()
        resultado = analisador.analisar(texto, criterios_ativos)

        # Limpar
        try:
            os.remove(filepath)
        except:
            pass

        return resultado

    except Exception as e:
        # Catch specific exception
        raise e

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
    # Restrict server binding to localhost