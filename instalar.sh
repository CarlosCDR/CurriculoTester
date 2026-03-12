#!/bin/bash

# Script de instalação das dependências do Avaliador de Currículos

echo "================================"
echo "Avaliador de Currículos em PDF"
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
pip3 install -r requirements.txt

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
echo "Para iniciar a aplicação, execute:"
echo "  python3 main.py"
echo ""
