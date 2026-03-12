# 📚 Guia Completo de Uso - Avaliador de Currículos

## 1. Primeiros Passos

### Instalação Rápida

**Windows:**
```bash
1. Abra o PowerShell ou CMD
2. Navegue para a pasta do projeto
3. Execute: instalar.bat
4. Execute: python main.py
```

**Linux/macOS:**
```bash
1. Abra o Terminal
2. Navegue para a pasta do projeto
3. Execute: chmod +x instalar.sh
4. Execute: ./instalar.sh
5. Execute: python3 main.py
```

### Instalação Manual

```bash
# 1. Instale as dependências
pip install PyPDF2

# 2. Execute a aplicação
python main.py
```

---

## 2. Interface da Aplicação

### Áreas Principais

```
┌─────────────────────────────────────────────────────┐
│  Avaliador de Currículos                            │
├─────────────────────────────────────────────────────┤
│ 📄 Seleção de Currículo                             │
│ [Nenhum arquivo selecionado] [Carregar PDF]         │
├─────────────────────────────────────────────────────┤
│ 🎯 Critérios de Avaliação                           │
│ ☑ Experiência (Peso: 25%)                           │
│ ☑ Formação Educacional (Peso: 20%)                  │
│ ☑ Habilidades Técnicas (Peso: 30%)                  │
│ ☑ Certificações (Peso: 15%)                         │
│ ☑ Idiomas (Peso: 10%)                               │
├─────────────────────────────────────────────────────┤
│ [🔍 Analisar Currículo] [🗑️ Limpar]                 │
├─────────────────────────────────────────────────────┤
│ 📊 Resultados                                       │
│                                                     │
│ (Resultado aparecerá aqui)                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 3. Passo a Passo de Uso

### Etapa 1: Selecionar um Currículo

1. Clique no botão **"Carregar PDF"**
2. Navegue até o arquivo do currículo em PDF
3. Clique em **"Abrir"**
4. O nome do arquivo aparecerá com um ✓ verde

### Etapa 2: Configurar Critérios

Os critérios padrão já estão configurados, mas você pode:
- **Desativar criterios**: Desmarque os ☑️ que não deseja usar
- **Aumentar importância**: Note que "Habilidades Técnicas" tem peso 30% (mais importante)
- **Combinar critérios**: Selecione apenas os relevantes para a vaga

### Etapa 3: Executar Análise

1. Clique em **"🔍 Analisar Currículo"**
2. Aguarde o processamento (alguns segundos)
3. Veja os resultados aparecerem na área de texto

### Etapa 4: Interpretar Resultados

```
═════════════════════════════════════════════════════
AVALIAÇÃO DE CURRÍCULO
═════════════════════════════════════════════════════
Data: 10/03/2026 14:35:21
Arquivo: joao_silva.pdf
═════════════════════════════════════════════════════

📈 PONTUAÇÃO GERAL: 75.50/100

✅ PONTOS POSITIVOS:
  ✓ Experiência: Encontradas 8 correspondências relevantes
  ✓ Habilidades Técnicas: Encontradas 12 correspondências
  ✓ Formação Educacional: Encontradas 4 correspondências

❌ PONTOS NEGATIVOS:
  ✗ Certificações: Apenas 1 correspondência encontrada
  ✗ Idiomas: Apenas 2 correspondências encontradas

─────────────────────────────────────────────────
📋 DETALHES POR CRITÉRIO:
─────────────────────────────────────────────────

Experiência:
  Pontuação: 90.0%
  Peso: 25%
  Correspondências: 8

Formação Educacional:
  Pontuação: 80.0%
  Peso: 20%
  Correspondências: 4

[...]

─────────────────────────────────────────────────
💡 RECOMENDAÇÕES:
─────────────────────────────────────────────────
✅ Currículo com boa compatibilidade
📝 Considere destacar mais as habilidades e experiências
═════════════════════════════════════════════════════
```

---

## 4. Interpretando a Pontuação

| Pontuação | Nível | Significado |
|-----------|-------|-------------|
| 80-100 | ✅ Excelente | Muito bem alinhado com os critérios |
| 60-79 | ✓ Bom | Bem alinhado, pode faltar algo |
| 40-59 | ⚠️ Moderado | Compatibilidade aceitável |
| 0-39 | ❌ Baixo | Pouca compatibilidade |

---

## 5. Casos de Uso Avançados

### Use Case 1: Avaliar Desenvolvedor Python

**Objetivo:** Encontrar um desenvolvedor Python com experiência

**Configuração:**
1. Desmarque "Idiomas" (menos importante)
2. Mantenha "Habilidades Técnicas" marcado (peso 30%)
3. Aumente mentalmente a importância de Python nas habilidades

**Interpretação:**
- Se Python aparece nas "Habilidades Técnicas": ✓ Positivo
- Se tem 5+ anos de experiência: ✓ Positivo
- Se não tem certificações: ✗ Negativo (mas não crítico)

### Use Case 2: Buscar Profissional Sênior

**Objetivo:** Encontrar profissional com muita experiência

**Configuração:**
1. Aumente o peso mentalmente para "Experiência"
2. Procure por "5 anos", "10 anos", "sênior"
3. Priorize "Habilidades Técnicas" e "Certificações"

**Análise esperada:**
- Pontuação > 75 = Candidato forte
- Múltiplas certificações = Extra positivo

### Use Case 3: Avaliar Entry-Level

**Objetivo:** Encontrar junior/estagiário promissor

**Configuração:**
1. Desmarque "Experiência" como requisito crítico
2. Priorize "Formação Educacional" e "Habilidades Técnicas"
3. Procure por bootcamps, cursos online
4. Valide certificações de formação

**Análise esperada:**
- Criação de portfólio = + Positivo
- Projetos pessoais mencionados = Excelente sinal
- Formação educacional = Essencial

---

## 6. Customização Avançada

### Modificar Pesos dos Critérios

**Arquivo:** `criterios.json`

```json
{
  "criterios": {
    "Experiência": {
      "peso": 35  // Aumentado de 25 para 35
    },
    "Habilidades Técnicas": {
      "peso": 40  // Aumentado de 30 para 40
    }
  }
}
```

### Adicionar Novas Habilidades Técnicas

**Arquivo:** `criterios.json`

```json
{
  "Habilidades Técnicas": {
    "palabras_chave": [
      "python",
      "javascript",
      "meu_novo_framework",  // Adicione aqui
      "outra_tecnologia"
    ]
  }
}
```

### Criar Critério Customizado

No `main.py`, adicione um novo critério:

```python
CRITERIOS_PREDEFINIDOS = {
    # ... critérios existentes ...
    
    "Liderança": {
        "descricao": "Experiência em liderança de equipes",
        "peso": 20,
        "palestras_chave": ["líder", "liderança", "gerente", "coordenador", "supervisor"],
        "tipo": "lista"
    }
}
```

---

## 7. Dicas e Truques

### 💡 Dica 1: Análise em Lote
- Abra múltiplas cópias da aplicação
- Analise 2-3 currículos em paralelo
- Compare as pontuações lado a lado

### 💡 Dica 2: Pesquisa no PDF
- Alguns PDFs contêm mais informações em rodapés
- Se a análise retornar baixa pontuação mas visualmente vê habilidades
- Tente editar o critério para incluir variações de palavras-chave

### 💡 Dica 3: Relatório Manual
- Copie os resultados da análise (Select All + Copy)
- Cole em um arquivo Word/Google Docs
- Crie um arquivo de comparação entre candidatos

### 💡 Dica 4: Validação Cruzada
- Sempre valide a análise lendo o currículo manualmente
- O sistema é uma ferramenta de suporte, não decisão final
- Combine dados quantitativos com análise qualitativa

---

## 8. Troubleshooting

### Problema: "Erro: PyPDF2 não instalado"
```bash
# Solução
pip install PyPDF2
# ou
pip install PyPDF2==3.0.1
```

### Problema: PDF não é processado
**Causas possíveis:**
- PDF é apenas imagem (sem texto)
- PDF está corrompido
- PDF tem permissões de segurança

**Solução:**
- Tente converter o PDF com ferramenta online
- Use outro PDF para testar
- Extraia o texto manualmente e copie

### Problema: Pontuação muito baixa
**Verificar:**
1. Os critérios estão corretos para a vaga?
2. As palavras-chave estão corretas?
3. O currículo tem as informações em inglês ou português?

**Solução:**
- Customize os critérios para a vaga específica
- Adicione variações de palavras-chave (ex: "dev" + "developer")

### Problema: Aplicação lenta
**Causas:**
- PDF muito grande ou com muitas páginas
- Computador com pouca RAM

**Solução:**
- Reduza tamanho do PDF
- Feche outros programas
- Reinicie a aplicação

---

## 9. Exemplos de Palavras-Chave por Profissão

### Desenvolvedor Python
```
python, django, flask, fastapi, asyncio, 
pandas, numpy, scikit-learn, api, rest
```

### Desenvolvedor Web (Front-end)
```
react, vue, angular, javascript, typescript,
html5, css3, webpack, npm, node, responsive
```

### DevOps Engineer
```
docker, kubernetes, ci/cd, jenkins, aws, azure,
terraform, ansible, linux, git, automação
```

### Data Scientist
```
python, r, sql, machine learning, tensorflow,
pytorch, estatística, análise, dashboards
```

### Gerente de Projetos
```
scrum, agile, pmp, comunicação, liderança,
stakeholder, jira, planejamento, equipe
```

---

## 10. Contato e Suporte

- 📧 Para bugs ou sugestões
- 🐙 Contribua com melhorias no GitHub
- 📖 Leia documentação completa no README.md

---

**Última atualização:** 10/03/2026
**Versão:** 1.0
