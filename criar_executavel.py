#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de executável para o Avaliador de Currículos
Cria um .exe standalone usando PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def verificar_pyinstaller():
    """Verifica se PyInstaller está instalado"""
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado")
        return True
    except ImportError:
        print("❌ PyInstaller não encontrado")
        print("Instalando PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller instalado com sucesso")
            return True
        except subprocess.CalledProcessError:
            print("❌ Falha ao instalar PyInstaller")
            return False

def criar_icone():
    """Cria um ícone simples usando Python"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        import io

        # Criar imagem 256x256
        img = Image.new('RGBA', (256, 256), (70, 130, 180, 255))  # Steel blue
        draw = ImageDraw.Draw(img)

        # Desenhar um documento com ícone de análise
        # Fundo do documento
        draw.rectangle([50, 50, 206, 206], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=3)

        # Linhas do documento
        draw.line([70, 80, 186, 80], fill=(0, 0, 0, 255), width=2)
        draw.line([70, 100, 186, 100], fill=(0, 0, 0, 255), width=2)
        draw.line([70, 120, 186, 120], fill=(0, 0, 0, 255), width=2)
        draw.line([70, 140, 160, 140], fill=(0, 0, 0, 255), width=2)

        # Ícone de análise (lupa)
        # Cabo da lupa
        draw.ellipse([160, 160, 190, 190], fill=(255, 215, 0, 255), outline=(0, 0, 0, 255), width=2)
        # Lente da lupa
        draw.ellipse([140, 140, 180, 180], fill=(255, 255, 255, 200), outline=(0, 0, 0, 255), width=2)
        # Alça da lupa
        draw.arc([150, 150, 170, 170], start=45, end=135, fill=(0, 0, 0, 255), width=3)

        # Salvar como ICO
        img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
        print("✅ Ícone criado: icon.ico")
        return True

    except ImportError:
        print("⚠️  PIL não encontrado. Criando ícone básico...")
        # Criar ícone básico sem PIL
        try:
            # Criar um ícone simples usando tkinter
            import tkinter as tk
            from tkinter import PhotoImage
            import base64

            # Ícone simples em base64 (16x16 pixels)
            icon_data = """
            R0lGODlhEAAQAIAAAAAAAP///yH5BAEAAAAALAAAAAAQABAAAAIhhI+py+0Po5y02ouz3rz7D4biSJbmiabqyrbuC8fyTNf2j
            """

            with open('icon.ico', 'wb') as f:
                f.write(base64.b64decode(icon_data))
            print("✅ Ícone básico criado")
            return True

        except Exception as e:
            print(f"❌ Falha ao criar ícone: {e}")
            return False

def criar_spec_file():
    """Cria arquivo .spec personalizado para PyInstaller"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('criterios.json', '.'),
        ('exemplos_vagas.json', '.'),
        ('README.md', '.'),
        ('GUIA_COMPLETO.md', '.'),
        ('FAQ.md', '.'),
        ('QUICK_REFERENCE.md', '.'),
        ('ARQUITETURA.md', '.'),
        ('CHANGELOG.md', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AvaliadorCurriculos',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)
'''

    with open('AvaliadorCurriculos.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)

    print("✅ Arquivo .spec criado: AvaliadorCurriculos.spec")
    return True

def criar_executavel():
    """Cria o executável usando PyInstaller"""
    print("\n" + "="*60)
    print("CRIANDO EXECUTÁVEL")
    print("="*60)

    try:
        # Comando PyInstaller
        cmd = [
            sys.executable, "-m", "pyinstaller",
            "--onefile",  # Executável único
            "--windowed",  # Sem console
            "--icon=icon.ico",
            "--name=AvaliadorCurriculos",
            "--add-data=criterios.json;.",
            "--add-data=exemplos_vagas.json;.",
            "--add-data=README.md;.",
            "--add-data=GUIA_COMPLETO.md;.",
            "--add-data=FAQ.md;.",
            "--add-data=QUICK_REFERENCE.md;.",
            "--add-data=ARQUITETURA.md;.",
            "--add-data=CHANGELOG.md;.",
            "main.py"
        ]

        print("Executando PyInstaller...")
        print("Comando:", " ".join(cmd))
        print("\nIsso pode levar alguns minutos...")

        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')

        if result.returncode == 0:
            print("✅ Executável criado com sucesso!")
            print("📁 Localização: dist/AvaliadorCurriculos.exe")

            # Verificar se o arquivo foi criado
            exe_path = Path("dist/AvaliadorCurriculos.exe")
            if exe_path.exists():
                size = exe_path.stat().st_size / (1024 * 1024)  # MB
                print(".2f"            else:
                print("⚠️  Arquivo executável não encontrado")

            return True
        else:
            print("❌ Falha ao criar executável")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False

    except Exception as e:
        print(f"❌ Erro durante criação: {e}")
        return False

def criar_instalador():
    """Cria um instalador simples"""
    print("\n" + "="*60)
    print("CRIANDO INSTALADOR")
    print("="*60)

    try:
        # Criar diretório do instalador
        installer_dir = Path("Instalador")
        installer_dir.mkdir(exist_ok=True)

        # Copiar executável
        exe_source = Path("dist/AvaliadorCurriculos.exe")
        exe_dest = installer_dir / "AvaliadorCurriculos.exe"

        if exe_source.exists():
            shutil.copy2(exe_source, exe_dest)
            print("✅ Executável copiado para instalador")
        else:
            print("❌ Executável não encontrado")
            return False

        # Criar script de instalação
        install_script = f'''@echo off
echo ========================================
echo    Avaliador de Currículos v1.0
echo ========================================
echo.
echo Instalando...
echo.

REM Criar atalho na área de trabalho
set "desktop=%USERPROFILE%\\Desktop"
set "target=%~dp0AvaliadorCurriculos.exe"
set "shortcut=%desktop%\\Avaliador de Currículos.lnk"

echo Criando atalho na área de trabalho...
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%shortcut%');$s.TargetPath='%target%';$s.Save()"

echo.
echo ✅ Instalação concluída!
echo.
echo Atalho criado na área de trabalho.
echo Clique duas vezes no ícone para iniciar.
echo.
pause
'''

        install_path = installer_dir / "instalar.bat"
        with open(install_path, 'w', encoding='utf-8') as f:
            f.write(install_script)

        # Criar README do instalador
        readme_content = '''# 📦 Instalador - Avaliador de Currículos

## Como Instalar

1. Execute `instalar.bat` como administrador
2. Um atalho será criado na área de trabalho
3. Clique duas vezes no ícone para iniciar

## O Que é Instalado

- ✅ Aplicação executável (AvaliadorCurriculos.exe)
- ✅ Atalho na área de trabalho
- ✅ Todos os arquivos necessários incluídos

## Requisitos

- Windows 7 ou superior
- Não requer instalação do Python

## Desinstalação

Simplesmente delete o atalho e o executável.

---
Versão 1.0 | 2026-03-11
'''

        readme_path = installer_dir / "LEIA-ME.txt"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print("✅ Instalador criado em: Instalador/")
        print("   ├── AvaliadorCurriculos.exe")
        print("   ├── instalar.bat")
        print("   └── LEIA-ME.txt")

        return True

    except Exception as e:
        print(f"❌ Erro ao criar instalador: {e}")
        return False

def limpar_arquivos_temporarios():
    """Remove arquivos temporários do PyInstaller"""
    print("\n" + "="*60)
    print("LIMPANDO ARQUIVOS TEMPORÁRIOS")
    print("="*60)

    dirs_to_remove = ["build", "dist", "__pycache__"]
    files_to_remove = ["AvaliadorCurriculos.spec"]

    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✅ Removido: {dir_name}/")
            except Exception as e:
                print(f"⚠️  Falha ao remover {dir_name}: {e}")

    for file_name in files_to_remove:
        if os.path.exists(file_name):
            try:
                os.remove(file_name)
                print(f"✅ Removido: {file_name}")
            except Exception as e:
                print(f"⚠️  Falha ao remover {file_name}: {e}")

def main():
    """Função principal"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 8 + "GERADOR DE EXECUTÁVEL - AVALIADOR DE CURRÍCULOS" + " " * 2 + "║")
    print("╚" + "=" * 58 + "╝\n")

    # Verificar PyInstaller
    if not verificar_pyinstaller():
        print("\n❌ PyInstaller necessário. Saindo...")
        return 1

    # Criar ícone
    if not criar_icone():
        print("\n⚠️  Continuando sem ícone personalizado...")

    # Criar executável
    if not criar_executavel():
        print("\n❌ Falha na criação do executável")
        return 1

    # Criar instalador
    if not criar_instalador():
        print("\n⚠️  Executável criado, mas instalador falhou")

    # Limpar temporários
    limpar_arquivos_temporarios()

    print("\n" + "="*60)
    print("✅ PROCESSO CONCLUÍDO!")
    print("="*60)
    print("\n📦 Instalador pronto em: Instalador/")
    print("   ├── AvaliadorCurriculos.exe (executável)")
    print("   ├── instalar.bat (script de instalação)")
    print("   └── LEIA-ME.txt (instruções)")
    print("\n🚀 Execute 'Instalador/instalar.bat' para instalar!")

    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Processo interrompido pelo usuário")
        exit_code = 1
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        exit_code = 1

    print("\n" + "="*60 + "\n")
    input("Pressione ENTER para sair...")
    sys.exit(exit_code)