#!/bin/bash

# Script de instalação da versão web do Avaliador de Currículos

echo "================================"
echo "Versao Web - Avaliador de Currículos"
echo "================================"
echo ""
echo "Instalando dependências..."
echo ""

# Verificar se pip está instalado
python3 -m pip --version > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Erro: Python3 e pip não encontrados"
    echo "Por favor, instale Python 3.7+ em https://www.python.org"
    exit 1
fi

# Instalar dependências
pip3 install -r requirements_web.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "Erro ao instalar dependências!"
    exit 1
fi

echo ""
echo "================================"
echo "Instalação concluída com sucesso!"
echo "================================"
echo ""
echo "Para iniciar a versão web, execute:"
echo "  python3 executar_web.py"
echo ""
echo "Ou diretamente:"
echo "  python3 app_web.py"
echo ""
echo "Acesse: http://localhost:5000"
echo ""