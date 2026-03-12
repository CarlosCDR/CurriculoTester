# ⚡ Quick Reference - Avaliador de Currículos

## 🚀 Início Rápido (5 minutos)

### 1. Instalar
```bash
# Windows
instalar.bat

# Linux/Mac
chmod +x instalar.sh && ./instalar.sh

# Manual
pip install PyPDF2
```

### 2. Executar
```bash
# Windows
python main.py

# Linux/Mac
python3 main.py
```

### 3. Usar
1. Clique "Carregar PDF"
2. Configure critérios (opcional)
3. Clique "Analisar Currículo"
4. Veja resultados

---

## 📁 Arquivos do Projeto

```
SPEED TEST/
├── main.py                 ← Aplicação principal
├── requirements.txt        ← Dependências Python
├── criterios.json         ← Critérios customizáveis
├── exemplos_vagas.json    ← Exemplos por profissão
├── README.md              ← Documentação geral
├── GUIA_COMPLETO.md       ← Guia detalhado
├── FAQ.md                 ← Perguntas frequentes
├── ARQUITETURA.md         ← Documentação técnica
├── testar_instalacao.py   ← Script de teste
├── instalar.bat           ← Instalador (Windows)
└── instalar.sh            ← Instalador (Linux/Mac)
```

---

## 🎯 Critérios Padrão & Pesos

| Critério | Peso | Busca |
|----------|------|-------|
| Experiência | 25% | anos, experiência, trabalho |
| Formação | 20% | graduação, mestrado, diploma |
| Habilidades | 30% | python, javascript, java, sql |
| Certificações | 15% | certificado, aws, google |
| Idiomas | 10% | inglês, espanhol, fluente |

---

## 💡 Casos de Uso Rápidos

### Dev Python Junior
Desmarcar "Idiomas", Priorizar "Formação" + "Habilidades Técnicas"

### Profissional Sênior
Aumentar peso "Experiência", Procurar "5+ anos"

### Análise de Dados
Foco em SQL, Python, BI (Tableau, Power BI)

### DevOps
Foco em Docker, Kubernetes, AWS, CI/CD

### Gerente de Projetos
Foco em Scrum, Agile, Liderança

---

## 📊 Interpretar Resultados

```
Pontuação 80-100 ✅   → Excelente compatibilidade
Pontuação 60-79  ✓    → Boa compatibilidade
Pontuação 40-59  ⚠️   → Compatibilidade moderada
Pontuação 0-39   ❌   → Baixa compatibilidade
```

---

## ⚙️ Customizar em 2 Passos

### Passo 1: Editar `criterios.json`
```json
{
  "criterios": {
    "Meu Critério": {
      "descricao": "O que avaliar",
      "peso": 25,
      "palavras_chave": ["palavra1", "palavra2"],
      "tipo": "lista"
    }
  }
}
```

### Passo 2: Executar
```bash
python main.py
# Novo critério aparecerá automaticamente
```

---

## 🔧 Comandos Úteis

### Testar Instalação
```bash
python testar_instalacao.py
```

### Reinstalar Dependências
```bash
pip install --upgrade PyPDF2
```

### Verificar Python
```bash
python --version
# ou
python3 --version
```

### Versão Específica (Linux/Mac)
```bash
python3 testar_instalacao.py
python3 main.py
```

---

## 🐛 Troubleshooting Rápido

| Problema | Solução |
|----------|---------|
| "Python não encontrado" | Use `python3` em vez de `python` |
| "PyPDF2 não instalado" | `pip install PyPDF2` |
| "Tkinter não encontrado" | Reinstale Python com tcl/tk |
| "PDF não processa" | Verifique se PDF tem texto (não é imagem) |
| "Baixa pontuação" | Customize critérios para a vaga |

---

## 📋 Fórmulas & Conceitos

### Cálculo de Pontuação
```
Para cada critério:
  Correspondências = Encontradas / Total Palavras-chave
  Pontos = Correspondências × Peso
Pontuação Final = Soma todos os Pontos / Peso Total
```

### Exemplo
```
Critério: Habilidades (peso 30%)
Palavras: ["python", "java", "sql"]
Encontrou: ["python", "sql"]
Score = (2/3) × 100 = 66.7%
Contribuição = 66.7 × 0.30 = 20 pontos
```

---

## 📚 Documentação

| Arquivo | Conteúdo |
|---------|----------|
| README.md | Visão geral, instalação, uso basics |
| GUIA_COMPLETO.md | Casos avançados, customização |
| FAQ.md | Perguntas frequentes |
| ARQUITETURA.md | Código, estrutura, extensibilidade |

**Leitura recomendada:**
1. Comece com README.md
2. Se problemas → FAQ.md
3. Para customizar → GUIA_COMPLETO.md
4. Para entender código → ARQUITETURA.md

---

## 🎓 Exemplos Prontos

Veja `exemplos_vagas.json` para setups de:
- ✅ Desenvolvedor Python Junior
- ✅ Desenvolvedor Full Stack
- ✅ Analista de Dados
- ✅ DevOps Engineer
- ✅ Gerente de Projetos

Copie e adapte conforme necessidade!

---

## ✨ Dicas Pro

### 💡 Dica 1: Análise em Lote
```bash
# Abra 2+ instâncias
python main.py &
python main.py &
```

### 💡 Dica 2: Criar Preset para Vaga
```bash
# Crie arquivo específico
cp criterios.json criterios_dev_python.json
# Edite conforme vaga
# Depois copie de volta antes de usar
```

### 💡 Dica 3: Validação Manual
- Sistema acha habilidades automaticamente
- Valide lendo currículo visualmente
- Combine automático + manual = melhor resultado

### 💡 Dica 4: Palavras-Chave Importantes
Adicione variações:
- "developer" + "dev" + "desenvolvedor"
- "machine learning" + "ml" + "ia"
- "kubernetes" + "k8s"

---

## 🚀 Próximos Passos

1. **Instale:** `instalar.bat` (5 min)
2. **Teste:** Carregue um PDF de test (2 min)
3. **Customize:** Ajuste critérios (5 min)
4. **Use:** Analise seus currículos (ongoing)

---

## 💬 Atalhos Teclado

| Ação | Teclado |
|------|---------|
| Selecionar arquivo | Ctrl+Clique em "Carregar PDF" |
| Copiar resultado | Ctrl+A depois Ctrl+C |
| Limpar tudo | Clique "Limpar" |
| Imprimir | Ctrl+P |

---

## 📞 Help & Support

- **Erro de instalação?** → Veja FAQ.md
- **Como usar avançado?** → Veja GUIA_COMPLETO.md  
- **Quer entender código?** → Veja ARQUITETURA.md
- **Não encontrou?** → Execute `testar_instalacao.py`

---

## 📌 Checklist Primeiro Uso

- [ ] Instalar dependências
- [ ] Executar testar_instalacao.py
- [ ] Abrir main.py
- [ ] Carregar PDF de teste
- [ ] Configurar critérios
- [ ] Analisar
- [ ] Revisar resultado
- [ ] Customizar conforme necessário

---

## 🔐 Segurança & Privacidade

✅ **Seguro:**
- Trabalha 100% offline
- Nenhum dado enviado
- Arquivo local apenas
- Open source

---

## 📊 Estatísticas Rápidas

- **Tempo instalação:** ~2 minutos
- **Tempo análise PDF:** ~1-2 segundos
- **Tamanho do projeto:** ~50 KB
- **Dependências:** 1 (PyPDF2)
- **Compatibilidade:** Windows, Linux, macOS

---

**Versão:** 1.0  
**Última atualização:** 10/03/2026  
**Status:** ✅ Pronto para produção
