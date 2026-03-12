#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para executar a versão web do Avaliador de Currículos
"""

import os
import sys
import subprocess

def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    try:
        import flask
        import PyPDF2
        print("✅ Dependências encontradas")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("\nInstalando dependências...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_web.txt"])
            print("✅ Dependências instaladas")
            return True
        except subprocess.CalledProcessError:
            print("❌ Falha ao instalar dependências")
            return False

def executar_web():
    """Executa a aplicação web"""
    try:
        print("\n" + "="*60)
        print("🚀 INICIANDO VERSÃO WEB")
        print("="*60)
        print("📱 Interface Web: http://localhost:5000")
        print("❌ Para parar: Ctrl+C")
        print("="*60 + "\n")

        # Executar Flask
        from app_web import app
        app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)

    except KeyboardInterrupt:
        print("\n\n👋 Aplicação web parada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao executar aplicação web: {e}")
        return False

    return True

def main():
    """Função principal"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 12 + "VERSÃO WEB - AVALIADOR DE CURRÍCULOS" + " " * 6 + "║")
    print("╚" + "=" * 58 + "╝\n")

    # Verificar dependências
    if not verificar_dependencias():
        print("\n❌ Problemas com dependências. Saindo...")
        return 1

    # Executar aplicação
    if not executar_web():
        return 1

    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        exit_code = 1

    print("\n" + "="*60 + "\n")
    input("Pressione ENTER para sair...")
    sys.exit(exit_code)