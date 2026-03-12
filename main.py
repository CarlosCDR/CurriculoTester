import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json
import os
from datetime import datetime
import re
import language_tool_python
from docx import Document
from fpdf import FPDF

# Importar bibliotecas para PDF
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None


class CriterioCurriculo:
    """Define critérios para avaliação de currículos"""
    
    CRITERIOS_PREDEFINIDOS = {
        "Experiência": {
            "descricao": "Anos de experiência na área",
            "peso": 25,
            "palavras_chave": ["experiência", "anos", "trabalho", "profissional"],
            "tipo": "numerico"
        },
        "Formação Educacional": {
            "descricao": "Nível de educação formal",
            "peso": 20,
            "palavras_chave": ["graduação", "mestrado", "doutorado", "bacharel", "diploma", "faculdade"],
            "tipo": "categorico"
        },
        "Habilidades Técnicas": {
            "descricao": "Competências técnicas relevantes",
            "peso": 30,
            "palavras_chave": ["python", "javascript", "java", "sql", "react", "node", "docker", "aws", "linux"],
            "tipo": "lista"
        },
        "Certificações": {
            "descricao": "Certificações profissionais",
            "peso": 15,
            "palavras_chave": ["certificado", "certificação", "certified", "aws", "google", "microsoft"],
            "tipo": "lista"
        },
        "Idiomas": {
            "descricao": "Conhecimento de idiomas",
            "peso": 10,
            "palavras_chave": ["inglês", "espanhol", "português", "francês", "fluente", "intermediário"],
            "tipo": "lista"
        }
    }


class ProcessadorPDF:
    """Processa e extrai texto de arquivos PDF"""
    
    @staticmethod
    def extrair_texto(caminho_pdf):
        """Extrai texto de um arquivo PDF"""
        try:
            if not PyPDF2:
                return "Erro: PyPDF2 não instalado. Instale com: pip install PyPDF2"
            
            texto_completo = ""
            with open(caminho_pdf, 'rb') as arquivo:
                leitor = PyPDF2.PdfReader(arquivo)
                for pagina in leitor.pages:
                    texto_completo += pagina.extract_text() + "\n"
            
            return texto_completo.lower()
        except Exception as e:
            return f"Erro ao processar PDF: {str(e)}"


class AnalisadorCurriculo:
    """Analisa e avalia currículos com base em critérios"""
    
    def __init__(self, criterios_customizados=None):
        self.criterios = criterios_customizados or CriterioCurriculo.CRITERIOS_PREDEFINIDOS
    
    def analisar(self, texto_curriculo, criterios_ativos=None):
        """Analisa o currículo e retorna avaliação"""
        if criterios_ativos is None:
            criterios_ativos = list(self.criterios.keys())

        resultados = {
            "pontos_positivos": [],
            "pontos_negativos": [],
            "pontuacao_total": 0,
            "detalhes_criterios": {}
        }

        pontuacao_acumulada = 0
        peso_total = 0

        for criterio, config in self.criterios.items():
            if criterio not in criterios_ativos:
                continue

            peso = config.get("peso", 10)
            palavras_chave = config.get("palavras_chave", [])

            # Contar correspondências
            match_count = sum(1 for palavra in palavras_chave if palavra in texto_curriculo)
            pontuacao_criterio = min(100, (match_count / max(1, len(palavras_chave))) * 100)

            # Armazenar resultado detalhado do critério
            resultados["detalhes_criterios"][criterio] = {
                "pontuacao": pontuacao_criterio,
                "peso": peso,
                "correspondencias": match_count,
                "palavras_chave_encontradas": [palavra for palavra in palavras_chave if palavra in texto_curriculo],
                "palavras_chave_faltantes": [palavra for palavra in palavras_chave if palavra not in texto_curriculo]
            }

            # Adicionar ao acumulado
            pontuacao_acumulada += (pontuacao_criterio * peso) / 100
            peso_total += peso

            # Classificar como positivo ou negativo
            if pontuacao_criterio >= 60:
                resultados["pontos_positivos"].append(
                    f"✓ {criterio}: {match_count} correspondências relevantes encontradas"
                )
            else:
                resultados["pontos_negativos"].append(
                    f"✗ {criterio}: Apenas {match_count} correspondências encontradas"
                )

        # Calcular pontuação final
        if peso_total > 0:
            resultados["pontuacao_total"] = round(pontuacao_acumulada / peso_total, 2)

        # Adicionar recomendações detalhadas
        resultados["recomendacoes"] = self._gerar_recomendacoes(resultados)

        return resultados

    def _gerar_recomendacoes(self, resultados):
        """Gera recomendações detalhadas de melhoria"""
        recomendacoes = []

        if resultados["pontuacao_total"] < 50:
            recomendacoes.append("⚠️  Currículo com baixa compatibilidade com os critérios. Considere revisar os pontos negativos.")
        elif resultados["pontuacao_total"] < 70:
            recomendacoes.append("ℹ️  Currículo com compatibilidade moderada. Há espaço para melhorias.")
        else:
            recomendacoes.append("✅ Currículo com boa compatibilidade. Continue aprimorando!")

        for criterio, detalhes in resultados["detalhes_criterios"].items():
            if detalhes["pontuacao"] < 60:
                recomendacoes.append(
                    f"🔍 Para o critério '{criterio}', destaque mais as seguintes palavras-chave: {', '.join(detalhes['palavras_chave_faltantes'])}"
                )

        return recomendacoes


class OtimizadorCurriculo:
    """Classe para otimizar currículos para ATS"""

    def __init__(self):
        self.tool = language_tool_python.LanguageTool('pt-BR')

    def corrigir_texto(self, texto):
        """Corrige erros de português e inglês no texto"""
        return self.tool.correct(texto)

    def organizar_curriculo(self, dados):
        """Reorganiza o currículo em seções otimizadas para ATS"""
        return {
            "Contato": dados.get("contato", ""),
            "Objetivo": dados.get("objetivo", ""),
            "Formação Acadêmica": dados.get("formacao", ""),
            "Competências Técnicas": dados.get("competencias", ""),
            "Experiência de Projetos": dados.get("projetos", ""),
            "Experiência Profissional": dados.get("experiencia", ""),
            "Certificações": dados.get("certificacoes", ""),
            "Outras Experiências": dados.get("outras", ""),
        }

    def gerar_bullet_points(self, texto):
        """Transforma textos longos em bullet points"""
        return [f"• {linha.strip()}" for linha in texto.split(".") if linha.strip()]

    def adicionar_palavras_chave(self, texto):
        """Adiciona palavras-chave relevantes ao texto"""
        palavras_chave = ["desenvolvimento de software", "backend", "frontend", "mobile", "APIs", "metodologias ágeis", "estruturas de dados"]
        for palavra in palavras_chave:
            if palavra not in texto:
                texto += f" {palavra}"
        return texto

    def gerar_pdf(self, dados):
        """Gera o currículo final em PDF"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for secao, conteudo in dados.items():
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(200, 10, txt=secao, ln=True, align="L")
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, conteudo)
        pdf.output("curriculo_otimizado.pdf")

    def gerar_docx(self, dados):
        """Gera o currículo final em DOCX"""
        doc = Document()
        for secao, conteudo in dados.items():
            doc.add_heading(secao, level=1)
            doc.add_paragraph(conteudo)
        doc.save("curriculo_otimizado.docx")


class InterfaceAvaliador:
    """Interface gráfica para avaliação de currículos"""
    
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Avaliador de Currículos")
        self.janela.geometry("900x700")
        self.janela.resizable(True, True)
        
        self.analisador = AnalisadorCurriculo()
        self.file_path = None
        self.criterios_selecionados = dict.fromkeys(CriterioCurriculo.CRITERIOS_PREDEFINIDOS.keys(), True)
        
        self._criar_interface()
    
    def _criar_interface(self):
        """Cria a interface da aplicação"""
        # Frame superior para arquivo
        frame_arquivo = ttk.LabelFrame(self.janela, text="📄 Seleção de Currículo", padding=10)
        frame_arquivo.pack(fill="x", padx=10, pady=10)
        
        self.label_arquivo = ttk.Label(frame_arquivo, text="Nenhum arquivo selecionado", foreground="gray")
        self.label_arquivo.pack(side="left", padx=5)
        
        btn_carregar = ttk.Button(frame_arquivo, text="Carregar PDF", command=self._carregar_pdf)
        btn_carregar.pack(side="right", padx=5)
        
        # Frame para critérios
        frame_criterios = ttk.LabelFrame(self.janela, text="🎯 Critérios de Avaliação", padding=10)
        frame_criterios.pack(fill="both", expand=False, padx=10, pady=10)
        
        self.vars_criterios = {}
        for criterio, config in CriterioCurriculo.CRITERIOS_PREDEFINIDOS.items():
            var = tk.BooleanVar(value=True)
            self.vars_criterios[criterio] = var
            
            frame_crit = ttk.Frame(frame_criterios)
            frame_crit.pack(fill="x", pady=5)
            
            check = ttk.Checkbutton(frame_crit, text=criterio, variable=var)
            check.pack(side="left")
            
            label_desc = ttk.Label(
                frame_crit, 
                text=f"({config['descricao']})", 
                foreground="gray",
                font=("Arial", 8)
            )
            label_desc.pack(side="left", padx=20)
            
            label_peso = ttk.Label(
                frame_crit,
                text=f"Peso: {config['peso']}%",
                foreground="blue",
                font=("Arial", 8, "bold")
            )
            label_peso.pack(side="right")
        
        # Frame para botões de ação
        frame_botoes = ttk.Frame(self.janela)
        frame_botoes.pack(fill="x", padx=10, pady=10)
        
        btn_analisar = ttk.Button(frame_botoes, text="🔍 Analisar Currículo", command=self._analisar)
        btn_analisar.pack(side="left", padx=5)
        
        btn_limpar = ttk.Button(frame_botoes, text="🗑️  Limpar", command=self._limpar)
        btn_limpar.pack(side="left", padx=5)
        
        # Frame para resultados
        frame_resultado = ttk.LabelFrame(self.janela, text="📊 Resultados", padding=10)
        frame_resultado.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Text widget para resultados
        self.text_resultado = tk.Text(
            frame_resultado, 
            height=20, 
            width=100,
            font=("Courier", 9),
            bg="#f0f0f0"
        )
        self.text_resultado.pack(fill="both", expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_resultado, orient="vertical", command=self.text_resultado.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_resultado.config(yscrollcommand=scrollbar.set)
    
    def _carregar_pdf(self):
        """Carrega um arquivo PDF"""
        file_path = filedialog.askopenfilename(
            title="Selecione um currículo em PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if file_path:
            self.file_path = file_path
            nome_arquivo = os.path.basename(file_path)
            self.label_arquivo.config(text=f"✓ {nome_arquivo}", foreground="green")
    
    def _analisar(self):
        """Realiza a análise do currículo"""
        if not self.file_path:
            messagebox.showwarning("Aviso", "Por favor, selecione um arquivo PDF primeiro!")
            return
        
        # Extrair critérios selecionados
        criterios_ativos = [
            nome for nome, var in self.vars_criterios.items() if var.get()
        ]
        
        if not criterios_ativos:
            messagebox.showwarning("Aviso", "Selecione pelo menos um critério!")
            return
        
        # Processar PDF
        texto = ProcessadorPDF.extrair_texto(self.file_path)
        
        if texto.startswith("Erro"):
            messagebox.showerror("Erro", texto)
            return
        
        # Analisar
        resultado = self.analisador.analisar(texto, criterios_ativos)
        
        # Exibir resultados
        self._exibir_resultados(resultado)
    
    def _exibir_resultados(self, resultado):
        """Exibe os resultados da análise"""
        self.text_resultado.delete("1.0", tk.END)
        
        # Cabeçalho
        header = f"""
{'='*80}
AVALIAÇÃO DE CURRÍCULO
{'='*80}
Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Arquivo: {os.path.basename(self.file_path)}
{'='*80}

"""
        self.text_resultado.insert(tk.END, header)
        
        # Pontuação geral
        score_section = f"""
📈 PONTUAÇÃO GERAL: {resultado['pontuacao_total']}/100
{'─'*80}

"""
        self.text_resultado.insert(tk.END, score_section)
        
        # Pontos Positivos
        positivos = """✅ PONTOS POSITIVOS:
"""
        if resultado["pontos_positivos"]:
            for ponto in resultado["pontos_positivos"]:
                positivos += f"  {ponto}\n"
        else:
            positivos += "  Nenhum ponto positivo identificado\n"
        
        positivos += "\n"
        self.text_resultado.insert(tk.END, positivos)
        
        # Pontos Negativos
        negativos = """❌ PONTOS NEGATIVOS:
"""
        if resultado["pontos_negativos"]:
            for ponto in resultado["pontos_negativos"]:
                negativos += f"  {ponto}\n"
        else:
            negativos += "  Nenhum ponto negativo identificado\n"
        
        negativos += "\n"
        self.text_resultado.insert(tk.END, negativos)
        
        # Detalhes por Critério
        detalhes = """{'─'*80}
📋 DETALHES POR CRITÉRIO:
{'─'*80}
"""
        self.text_resultado.insert(tk.END, detalhes)
        
        for criterio, dados in resultado["detalhes_criterios"].items():
            linha = f"\n{criterio}:\n"
            linha += f"  Pontuação: {dados['pontuacao']:.1f}%\n"
            linha += f"  Peso: {dados['peso']}%\n"
            linha += f"  Correspondências: {dados['correspondencias']}\n"
            self.text_resultado.insert(tk.END, linha)
        
        # Recomendações
        recomendacoes = f"""
{'─'*80}
💡 RECOMENDAÇÕES:
{'─'*80}
"""
        for rec in resultado["recomendacoes"]:
            recomendacoes += f"{rec}\n"
        
        self.text_resultado.insert(tk.END, recomendacoes)
        
        # Rodapé
        footer = f"""
{'='*80}
"""
        self.text_resultado.insert(tk.END, footer)
    
    def _limpar(self):
        """Limpa os resultados"""
        self.text_resultado.delete("1.0", tk.END)
        self.file_path = None
        self.label_arquivo.config(text="Nenhum arquivo selecionado", foreground="gray")


# Inicializar aplicação
if __name__ == "__main__":
    janela = tk.Tk()
    app = InterfaceAvaliador(janela)
    janela.mainloop()