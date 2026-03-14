# 📄 Avaliador de Currículos em PDF

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Open%20Source-green)](LICENSE.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Sistema inteligente para avaliação automática de currículos em PDF com critérios customizáveis, análise detalhada e interface web moderna.**

[🚀 Começar](#-instalação) · [📖 Documentação](#-como-usar) · [🐛 Reportar Bug](https://github.com/CarlosCDR/CurriculoTester/issues) · [💡 Sugerir Feature](https://github.com/CarlosCDR/CurriculoTester/issues)

</div>

---

## 🎯 Funcionalidades

| Feature | Desktop | Web |
|---------|---------|-----|
| 📄 Leitura de PDF | ✅ | ✅ |
| 🎯 Critérios customizáveis | ✅ | ✅ |
| 📊 Pontuação automática | ✅ | ✅ |
| 💡 Recomendações de melhoria | ✅ | ✅ |
| 🌐 Acesso via browser | ❌ | ✅ |
| 📱 Mobile-friendly | ❌ | ✅ |
| 🔌 API REST | ❌ | ✅ |
| 💻 100% offline | ✅ | ✅ |

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                     Camada de Interface                   │
│         InterfaceAvaliador (Tkinter) │ Flask Web App      │
└──────────────────────┬──────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
┌────────────┐  ┌────────────┐  ┌────────────────┐
│ProcessadorPDF│  │AnalisadorCurriculo│  │CriterioCurriculo│
│  (PyPDF2)  │  │  (engine)  │  │  (JSON config)  │
└────────────┘  └────────────┘  └────────────────┘
```

**Componentes principais:**

- **`ProcessadorPDF`** – Extrai e normaliza texto de arquivos PDF via PyPDF2
- **`CriterioCurriculo`** – Define critérios de avaliação com pesos e palavras-chave
- **`AnalisadorCurriculo`** – Motor de análise que calcula pontuação ponderada por critério
- **`InterfaceAvaliador`** – Interface Tkinter para uso desktop
- **`app_web.py`** – Aplicação Flask com rotas web e API REST

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Versão Desktop

```bash
# 1. Clone o repositório
git clone https://github.com/CarlosCDR/CurriculoTester.git
cd CurriculoTester

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute
python main.py
```

> **Instaladores automáticos:**
> - Windows: `instalar.bat`
> - Linux/macOS: `./instalar.sh`

### Versão Web

```bash
# 1. Instale as dependências web
pip install -r requirements_web.txt

# 2. Execute o servidor
python executar_web.py

# 3. Acesse no browser
#    http://localhost:5000
```

> **Instaladores automáticos:**
> - Windows: `instalar_web.bat`
> - Linux/macOS: `./instalar_web.sh`

### Versão Executável Standalone

Gera um `.exe` sem necessidade de Python instalado:

```bash
python criar_executavel.py
# Resultado: Instalador/AvaliadorCurriculos.exe
```

---

## 📖 Como Usar

### Versão Desktop

1. Execute `python main.py`
2. Clique em **"Carregar PDF"** e selecione seu currículo
3. Ajuste os critérios e pesos conforme a vaga (opcional)
4. Clique em **"🔍 Analisar Currículo"**
5. Leia os resultados detalhados e as recomendações

### Versão Web

1. Execute `python executar_web.py`
2. Abra **http://localhost:5000** no browser
3. Faça o upload do PDF
4. Configure os critérios desejados
5. Clique em **"Analisar"** e visualize o relatório

### API REST

```bash
# Analisar currículo via cURL
curl -X POST http://localhost:5000/api/analisar \
  -F "file=@meu_curriculo.pdf" \
  -F "criterios=Habilidades Técnicas" \
  -F "criterios=Experiência"
```

**Resposta:**

```json
{
  "pontuacao_total": 72.5,
  "pontos_positivos": ["✓ Habilidades Técnicas: 5 correspondências encontradas"],
  "pontos_negativos": ["✗ Idiomas: Apenas 1 correspondência encontrada"],
  "detalhes_criterios": { "...": "..." },
  "recomendacoes": ["ℹ️ Currículo com compatibilidade moderada"]
}
```

---

## ⚙️ Customização de Critérios

### Critérios Predefinidos

| Critério | Peso | Descrição |
|----------|------|-----------|
| Experiência | 25% | Anos de experiência na área |
| Formação Educacional | 20% | Nível de educação formal |
| Habilidades Técnicas | 30% | Competências técnicas relevantes |
| Certificações | 15% | Certificações profissionais |
| Idiomas | 10% | Conhecimento de idiomas |

### Adicionando Critérios Personalizados

Edite o arquivo `criterios.json`:

```json
{
  "Liderança": {
    "descricao": "Experiência em gestão de equipes",
    "peso": 20,
    "palavras_chave": ["liderança", "equipe", "gestão", "coordenação", "mentor"],
    "tipo": "lista"
  }
}
```

### Templates por Profissão

O arquivo `exemplos_vagas.json` contém configurações prontas para:

- 🐍 Desenvolvedor Python Junior
- 🌐 Desenvolvedor Full Stack
- 📊 Analista de Dados
- 🐳 DevOps Engineer
- 📋 Gerente de Projetos

---

## 📊 Interpretando os Resultados

| Pontuação | Status | Significado |
|-----------|--------|-------------|
| ≥ 80 | ✅ Excelente | Alta compatibilidade com a vaga |
| 60–79 | ✓ Boa | Boa compatibilidade, pequenos ajustes recomendados |
| 40–59 | ⚠️ Moderada | Compatibilidade moderada, revise os pontos negativos |
| < 40 | ❌ Baixa | Currículo precisa de melhorias significativas |

---

## 📁 Estrutura do Projeto

```
CurriculoTester/
├── 📄 main.py                  # Interface Desktop (Tkinter) + motor de análise
├── 🌐 app_web.py               # Aplicação Web (Flask) + API REST
├── 🚀 executar_web.py          # Inicializador da versão web
├── 📦 criar_executavel.py      # Gerador de executável standalone
├── ✅ testar_instalacao.py     # Testes de verificação de instalação
├── 🔄 gerar_curriculo.py       # Gerador e otimizador de currículos
│
├── templates/                  # Templates HTML (versão web)
│   ├── base.html               # Layout base
│   ├── index.html              # Página inicial
│   ├── resultado.html          # Exibição de resultados
│   ├── configuracao.html       # Configuração de critérios
│   ├── ajuda.html              # Página de ajuda
│   └── sobre.html              # Sobre o projeto
│
├── criterios.json              # Critérios de avaliação customizáveis
├── exemplos_vagas.json         # Templates de critérios por profissão
├── requirements.txt            # Dependências da versão desktop
├── requirements_web.txt        # Dependências da versão web
│
├── instalar.bat / instalar.sh          # Instaladores desktop
├── instalar_web.bat / instalar_web.sh  # Instaladores web
│
├── README.md                   # Este arquivo
├── ARQUITETURA.md              # Documentação técnica detalhada
├── GUIA_COMPLETO.md            # Guia de uso completo
├── FAQ.md                      # Perguntas frequentes
├── QUICK_REFERENCE.md          # Referência rápida de comandos
└── CHANGELOG.md                # Histórico de versões
```

---

## 🐛 Solução de Problemas

<details>
<summary><b>PyPDF2 não instalado</b></summary>

```bash
pip install PyPDF2
```
</details>

<details>
<summary><b>Flask não encontrado</b></summary>

```bash
pip install -r requirements_web.txt
```
</details>

<details>
<summary><b>PDF não é processado corretamente</b></summary>

- Certifique-se de que o PDF contém texto selecionável (não apenas imagens escaneadas)
- PDFs gerados por ferramentas como Word/LibreOffice funcionam melhor
- Tente com outro arquivo PDF para verificar se o problema é específico do arquivo
</details>

<details>
<summary><b>Verificar instalação completa</b></summary>

```bash
python testar_instalacao.py
```
</details>

---

## 🗺️ Roadmap

- [x] Processamento de PDF com PyPDF2
- [x] Análise por palavras-chave com pesos configuráveis
- [x] Interface desktop com Tkinter
- [x] Interface web com Flask
- [x] API REST básica
- [x] Templates por profissão
- [ ] Suporte para DOCX e TXT
- [ ] Análise em lote de múltiplos currículos
- [ ] Machine Learning para análise semântica
- [ ] Dashboard com estatísticas e histórico
- [ ] Autenticação e múltiplos usuários
- [ ] Exportação de relatórios em PDF

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir.

```bash
# 1. Fork o projeto
# 2. Crie sua branch
git checkout -b feature/minha-feature

# 3. Commit suas mudanças
git commit -m "feat: adiciona suporte para DOCX"

# 4. Push para a branch
git push origin feature/minha-feature

# 5. Abra um Pull Request
```

---

## 📄 Licença

Este projeto é de código aberto sob a licença descrita em [LICENSE.md](LICENSE.md).

---

## 👨‍💻 Autor

**Carlos Daniel Rodrigues**

---

> **💡 Dica:** Escolha a versão que melhor se adapta ao seu uso:
> - **Desktop** → Uso individual offline, interface nativa
> - **Web** → Equipes, compartilhamento, acesso remoto
> - **Standalone** → Distribuição sem dependência de Python
