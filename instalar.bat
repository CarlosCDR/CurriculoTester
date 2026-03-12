@echo off
REM Script de instalação das dependências do Avaliador de Currículos

echo ================================
echo Avaliador de Currículos em PDF
echo ================================
echo.
echo Instalando dependências...
echo.

REM Verificar se pip está instalado
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo Erro: Python e pip não encontrados no PATH
    echo Por favor, instale Python 3.7+ em https://www.python.org
    exit /b 1
)

REM Instalar dependências
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Erro ao instalar dependências!
    exit /b 1
)

echo.
echo ================================
echo Instalação concluída com sucesso!
echo ================================
echo.
echo Para iniciar a aplicação, execute:
echo   python main.py
echo.
pause
