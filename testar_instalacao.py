#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de teste para validar a instalação do Avaliador de Currículos
Executa: python testar_instalacao.py
"""

import sys
import os
import json

def teste_python():
    """Verifica versão do Python"""
    print("=" * 60)
    print("1. VERIFICANDO VERSÃO DO PYTHON")
    print("=" * 60)
    
    version = sys.version_info
    print(f"Versão instalada: Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ ERRO: Python 3.7+ é obrigatório")
        return False
    else:
        print("✅ Python versão adequada")
        return True

def teste_tkinter():
    """Verifica se tkinter está disponível"""
    print("\n" + "=" * 60)
    print("2. VERIFICANDO TKINTER")
    print("=" * 60)
    
    try:
        import tkinter
        print("✅ Tkinter instalado e disponível")
        return True
    except ImportError as e:
        print(f"❌ ERRO: Tkinter não encontrado: {e}")
        print("\nSolução:")
        print("  Windows: Reinstale Python marcando 'tcl/tk and IDLE'")
        print("  Linux: pip install tk")
        print("  macOS: Geralmente incluído com Python")
        return False

def teste_pypdf2():
    """Verifica se PyPDF2 está instalado"""
    print("\n" + "=" * 60)
    print("3. VERIFICANDO PyPDF2")
    print("=" * 60)
    
    try:
        import PyPDF2
        print(f"✅ PyPDF2 versão {PyPDF2.__version__} instalado")
        return True
    except ImportError:
        print("❌ ERRO: PyPDF2 não encontrado")
        print("\nSolução:")
        print("  Execute: pip install PyPDF2")
        return False

def teste_arquivos():
    """Verifica se arquivos necessários existem"""
    print("\n" + "=" * 60)
    print("4. VERIFICANDO ARQUIVOS")
    print("=" * 60)
    
    arquivos_obrigatorios = [
        "main.py",
        "requirements.txt",
        "criterios.json"
    ]
    
    arquivos_opcionais = [
        "README.md",
        "GUIA_COMPLETO.md",
        "FAQ.md",
        "ARQUITETURA.md",
        "exemplos_vagas.json"
    ]
    
    todos_ok = True
    
    print("\nArquivos obrigatórios:")
    for arquivo in arquivos_obrigatorios:
        if os.path.exists(arquivo):
            tamanho = os.path.getsize(arquivo)
            print(f"  ✅ {arquivo} ({tamanho} bytes)")
        else:
            print(f"  ❌ {arquivo} - NÃO ENCONTRADO")
            todos_ok = False
    
    print("\nArquivos opcionais:")
    for arquivo in arquivos_opcionais:
        if os.path.exists(arquivo):
            tamanho = os.path.getsize(arquivo)
            print(f"  ✅ {arquivo} ({tamanho} bytes)")
        else:
            print(f"  ⚠️  {arquivo} - não encontrado (opcional)")
    
    return todos_ok

def teste_json():
    """Valida arquivos JSON"""
    print("\n" + "=" * 60)
    print("5. VALIDANDO JSON")
    print("=" * 60)
    
    arquivos_json = [
        "criterios.json",
        "exemplos_vagas.json"
    ]
    
    todos_ok = True
    
    for arquivo in arquivos_json:
        if os.path.exists(arquivo):
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"  ✅ {arquivo} - JSON válido")
            except json.JSONDecodeError as e:
                print(f"  ❌ {arquivo} - JSON inválido: {e}")
                todos_ok = False
        else:
            print(f"  ⚠️  {arquivo} - não encontrado")
    
    return todos_ok

def teste_modulos():
    """Testa importação de módulos principais"""
    print("\n" + "=" * 60)
    print("6. TESTANDO IMPORTAÇÕES")
    print("=" * 60)
    
    try:
        print("  Testando importações...")
        
        # Adicionar diretório atual ao path
        sys.path.insert(0, os.getcwd())
        
        # Tentar importar as classes principais
        from main import CriterioCurriculo, ProcessadorPDF, AnalisadorCurriculo
        
        print("  ✅ CriterioCurriculo importado com sucesso")
        print("  ✅ ProcessadorPDF importado com sucesso")
        print("  ✅ AnalisadorCurriculo importado com sucesso")
        
        # Verificar se critérios estão definidos
        criterios = CriterioCurriculo.CRITERIOS_PREDEFINIDOS
        print(f"  ✅ Critérios carregados: {len(criterios)} definidos")
        
        return True
    except Exception as e:
        print(f"  ❌ ERRO ao importar: {e}")
        return False

def teste_analise_simples():
    """Testa análise simples de texto"""
    print("\n" + "=" * 60)
    print("7. TESTE DE ANÁLISE SIMPLES")
    print("=" * 60)
    
    try:
        from main import AnalisadorCurriculo
        
        # Texto de teste
        texto_teste = """
        Desenvolvi softwares em Python e JavaScript anos.
        Tenho experiência com Django, Flask e React.
        Certificação AWS Solutions Architect.
        Falo Inglês fluente e Espanhol intermediário.
        """
        
        analisador = AnalisadorCurriculo()
        resultado = analisador.analisar(texto_teste)
        
        pontos_positivos = len(resultado.get("pontos_positivos", []))
        pontos_negativos = len(resultado.get("pontos_negativos", []))
        pontuacao = resultado.get("pontuacao_total", 0)
        
        print(f"\n  Texto de teste: {len(texto_teste)} caracteres")
        print(f"  Pontuação obtida: {pontuacao}/100")
        print(f"  Pontos positivos: {pontos_positivos}")
        print(f"  Pontos negativos: {pontos_negativos}")
        print(f"\n  ✅ Análise executada com sucesso!")
        
        return True
    except Exception as e:
        print(f"  ❌ ERRO na análise: {e}")
        import traceback
        traceback.print_exc()
        return False

def teste_gui():
    """Testa se UI pode ser inicializada"""
    print("\n" + "=" * 60)
    print("8. TESTE DA INTERFACE GRÁFICA")
    print("=" * 60)
    
    try:
        import tkinter as tk
        from main import InterfaceAvaliador
        
        print("  Criando janela de teste...")
        janela_teste = tk.Tk()
        janela_teste.withdraw()  # Ocultar janela
        
        app = InterfaceAvaliador(janela_teste)
        
        print("  ✅ Interface gráfica inicializada com sucesso")
        janela_teste.destroy()
        
        return True
    except Exception as e:
        print(f"  ❌ ERRO ao inicializar UI: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Executa todos os testes"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "TESTE DE INSTALAÇÃO - AVALIADOR DE CURRÍCULOS" + " " * 4 + "║")
    print("╚" + "=" * 58 + "╝\n")
    
    resultados = {
        "Python": teste_python(),
        "Tkinter": teste_tkinter(),
        "PyPDF2": teste_pypdf2(),
        "Arquivos": teste_arquivos(),
        "JSON": teste_json(),
        "Módulos": teste_modulos(),
        "Análise": teste_analise_simples(),
        "GUI": teste_gui()
    }
    
    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    passou = sum(1 for v in resultados.values() if v)
    total = len(resultados)
    
    for teste, resultado in resultados.items():
        simbolo = "✅" if resultado else "❌"
        print(f"{simbolo} {teste}")
    
    print("\n" + "-" * 60)
    print(f"Resultado: {passou}/{total} testes passaram")
    print("-" * 60)
    
    if passou == total:
        print("\n🎉 PERFEITO! Todas as verificações passaram!")
        print("\nVocê pode iniciar a aplicação com:")
        print("  python main.py")
        return 0
    elif passou >= 5:
        print("\n⚠️  ALGUNS TESTES FALHARAM")
        print("A aplicação pode funcionar, mas com limitações.")
        print("Execute os comandos sugeridos acima para corrigir.")
        return 1
    else:
        print("\n❌ INSTALAÇÃO INCOMPLETA")
        print("Execute os passos sugeridos nos testes acima.")
        return 2

if __name__ == "__main__":
    exit_code = main()
    print("\n" + "=" * 60 + "\n")
    
    # Pausa antes de fechar (Windows)
    try:
        if sys.platform == "win32":
            input("Pressione ENTER para sair...")
    except:
        pass
    
    sys.exit(exit_code)
