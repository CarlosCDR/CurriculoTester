# 📄 Avaliador de Currículos em PDF

Sistema inteligente para avaliação automática de currículos em PDF com critérios customizáveis e análise detalhada.

## 🎯 Funcionalidades

- ✅ Carregamento e processamento de arquivos PDF
- 🎯 Critérios de avaliação customizáveis (Experiência, Formação, Habilidades, Certificações, Idiomas)
- 📊 Pontuação automática baseada em critérios selecionados
- 💡 Recomendações de melhoria
- ✓/✗ Identificação de pontos positivos e negativos
- 📈 Análise detalhada por critério com pesos configuráveis
- 🔍 **Duas versões disponíveis: Desktop e Web**

## 🚀 Versões Disponíveis

### 🖥️ Versão Desktop (Recomendada)
Aplicação standalone com interface Tkinter. Ideal para uso individual e offline.

**Instalação:**
```bash
# Auto-instalação
instalar.bat  # Windows
./instalar.sh  # Linux/Mac

# Ou manual
pip install PyPDF2
python main.py
```

**Características:**
- ✅ Executável único (após instalação)
- ✅ Interface nativa
- ✅ 100% offline
- ✅ Instalador automático

### 🌐 Versão Web (Moderna)
Interface web moderna com Flask. Perfeita para compartilhamento e uso em equipe.

**Instalação:**
```bash
# Auto-instalação
instalar_web.bat  # Windows
./instalar_web.sh  # Linux/Mac

# Ou manual
pip install -r requirements_web.txt
python executar_web.py
```

**Características:**
- ✅ Interface Bootstrap moderna
- ✅ Mobile-friendly
- ✅ Compartilhamento de links
- ✅ API REST (futuro)
- 🌐 **Acesse:** http://localhost:5000

### 📦 Versão Instalável (Novo!)
Executável standalone sem necessidade de instalar Python.

**Criação:**
```bash
python criar_executavel.py
```

**Resultado:**
- 📁 `Instalador/AvaliadorCurriculos.exe`
- 📁 `Instalador/instalar.bat`
- 📁 `Instalador/LEIA-ME.txt`

## 📋 Critérios Predefinidos

| Critério | Peso | Descrição |
|----------|------|-----------|
| Experiência | 25% | Anos de experiência na área |
| Formação Educacional | 20% | Nível de educação formal |
| Habilidades Técnicas | 30% | Competências técnicas relevantes |
| Certificações | 15% | Certificações profissionais |
| Idiomas | 10% | Conhecimento de idiomas |

## 📖 Como Usar

### Versão Desktop
1. Execute `python main.py`
2. Clique "Carregar PDF"
3. Configure critérios (opcional)
4. Clique "Analisar Currículo"
5. Veja resultados

### Versão Web
1. Execute `python executar_web.py`
2. Abra http://localhost:5000
3. Upload do PDF
4. Configure critérios
5. Visualize análise

### Versão Instalável
1. Execute `Instalador/instalar.bat`
2. Clique no atalho criado
3. Use normalmente

## ⚙️ Customização

### Adicionar Novos Critérios

Edite `criterios.json`:

```json
{
  "Seu Critério": {
    "descricao": "Descrição do critério",
    "peso": 15,
    "palavras_chave": ["palavra1", "palavra2", "palavra3"],
    "tipo": "lista"
  }
}
```

### Templates por Profissão

Veja `exemplos_vagas.json` para configurações prontas:
- Desenvolvedor Python Junior
- Desenvolvedor Full Stack
- Analista de Dados
- DevOps Engineer
- Gerente de Projetos

## 📊 Interpretando os Resultados

- **Pontuação >= 80**: Excelente compatibilidade ✅
- **Pontuação 60-79**: Boa compatibilidade ✓
- **Pontuação 40-59**: Compatibilidade moderada ⚠️
- **Pontuação < 40**: Baixa compatibilidade ❌

## 📁 Estrutura do Projeto

```
SPEED TEST/
├── main.py                 # 🖥️ Versão Desktop
├── app_web.py             # 🌐 Versão Web (Flask)
├── criar_executavel.py    # 📦 Gerador de executável
├── executar_web.py        # 🚀 Executor versão web
├── testar_instalacao.py   # ✅ Testes de instalação
│
├── templates/             # 🌐 Templates web
│   ├── base.html
│   ├── index.html
│   ├── resultado.html
│   └── ...
│
├── criterios.json         # ⚙️ Critérios customizáveis
├── exemplos_vagas.json    # 📋 Templates por profissão
├── requirements.txt       # 📦 Deps desktop
├── requirements_web.txt   # 📦 Deps web
│
├── instalar.bat           # 🖥️ Instalador desktop
├── instalar.sh            # 🖥️ Instalador desktop (Linux)
├── instalar_web.bat       # 🌐 Instalador web
├── instalar_web.sh        # 🌐 Instalador web (Linux)
│
├── README.md              # 📖 Este arquivo
├── README_WEB.md          # 🌐 Documentação web
├── GUIA_COMPLETO.md       # 📚 Guia detalhado
├── FAQ.md                 # ❓ Perguntas frequentes
├── QUICK_REFERENCE.md     # ⚡ Referência rápida
├── ARQUITETURA.md         # 🏗️ Documentação técnica
└── CHANGELOG.md           # 📝 Histórico de versões
```

## 🐛 Solução de Problemas

### Versão Desktop
**"PyPDF2 não instalado"**
```bash
pip install PyPDF2
```

### Versão Web
**"Flask não encontrado"**
```bash
pip install -r requirements_web.txt
```

### Geral
**PDF não processado**
- Certifique-se que o PDF tem texto (não apenas imagem)
- Tente com outro PDF

## 🎓 Próximas Versões

- [ ] Suporte para DOCX e TXT
- [ ] Análise em lote de múltiplos currículos
- [ ] Machine Learning para análise mais precisa
- [ ] Dashboard web com estatísticas
- [ ] API REST completa
- [ ] Autenticação e usuários múltiplos

## 📄 Licença

Este projeto é de código aberto. Sinta-se livre para usar e modificar.

## 👨‍💻 Autor

Desenvolvido com ❤️ para ajudar na avaliação de currículos.

---

**Dica**: Escolha a versão que melhor se adapta ao seu uso:
- **Desktop**: Para uso individual offline
- **Web**: Para equipe e compartilhamento
- **Instalável**: Para distribuição sem Python
