# ❓ FAQ - Perguntas Frequentes

## Instalação e Setup

### P: Como instalar o programa?
**R:** Existem 3 formas:

1. **Automática (recomendado):**
   - Windows: Digite `instalar.bat`
   - Linux/Mac: Digite `./instalar.sh`

2. **Manual:**
   ```bash
   pip install PyPDF2
   python main.py
   ```

3. **Com Conda:**
   ```bash
   conda install PyPDF2
   python main.py
   ```

### P: Receive "Python não encontrado" ao executar
**R:** Python não está no PATH. Opções:

1. Instale Python novamente (marque "Add to PATH")
2. Use `python3` em vez de `python`:
   ```bash
   python3 main.py
   ```
3. Use caminho completo (exemplo Windows):
   ```bash
   C:\Users\seu_usuario\AppData\Local\Programs\Python\Python310\python.exe main.py
   ```

### P: Qual versão do Python é necessária?
**R:** Python 3.7 ou superior. Recomendado: Python 3.9+

---

## Uso e Funcionalidade

### P: Como analisar um currículo?
**R:** 
1. Clique em "Carregar PDF"
2. Selecione o arquivo do currículo
3. Configure os critérios (desmarque se necessário)
4. Clique em "Analisar Currículo"

### P: Posso analisar múltiplos currículos?
**R:** Sim, mas não simultaneamente na mesma janela. Opções:

1. Analise um, copie resultado, analise outro
2. Abra 2+ instâncias do programa (ctrl+clique instalar.bat)
3. Crie uma versão melhorada com análise em lote (veja seção "Desenvolvimento")

### P: Qual é a pontuação máxima possível?
**R:** 100 pontos. Interpretação:
- 80-100: Excelente
- 60-79: Bom
- 40-59: Moderado
- 0-39: Baixo

### P: A análise é 100% precisa?
**R:** Não. O sistema busca por palavras-chave, então:

**O que funciona bem:**
- Detectar tecnologias mencionadas
- Contar anos de experiência
- Validar certificações

**O que não funciona:**
- Avaliar qualidade de experiência
- Detectar "entre linhas"
- Julgar inteligência ou soft skills
- Ler contexto

**Dica:** Use como ferramenta de triagem, para análise final leia o currículo.

---

## Customização

### P: Como adicionar novos critérios?
**R:** Edite `criterios.json` e adicione:

```json
{
  "Novo Critério": {
    "descricao": "Descrição do critério",
    "peso": 15,
    "palavras_chave": ["palavra1", "palavra2", "palavra3"],
    "tipo": "lista"
  }
}
```

### P: Como aumentar/diminuir a importância de um critério?
**R:** Altere o valor `"peso"` em `criterios.json`:

```json
{
  "Habilidades Técnicas": {
    "peso": 40  // Aumentado (antes era 30)
  }
}
```

**Regra:** A soma de todos os pesos deve ser ~100.

### P: Como customizar para uma vaga específica?
**R:** 
1. Abra `exemplos_vagas.json` para ver padrões
2. Copie a estrutura para `criterios.json`
3. Customize as palavras-chave
4. Ajuste os pesos conforme importância

Por exemplo, para "Desenvolvedor Python":
```json
{
  "Habilidades Técnicas": {
    "peso": 40,
    "palavras_chave": ["python", "django", "flask", "fastapi", "sql"]
  },
  "Experiência": {
    "peso": 30,
    "palavras_chave": ["2 anos", "3 anos", "5 anos", "python"]
  }
}
```

### P: Posso ter critérios diferentes para vagas diferentes?
**R:** Atualmente o programa usa 1 arquivo de critérios. Opções:

1. **Simples:** Edite `criterios.json` toda vez
2. **Melhor:** Crie cópias nomeadas:
   - `criterios_python_dev.json`
   - `criterios_data_scientist.json`
   - `criterios_devops.json`
   Depois copie o arquivo correto para `criterios.json` antes de usar

3. **Profissional:** Desenvolva uma versão que leia arquivo de configuração dinâmica (veja próximas versões)

---

## PDFs e Documentos

### P: Que tipos de arquivo são suportados?
**R:** Atualmente apenas PDF com texto.

**Não suportado:**
- DOCX, DOC (Word)
- TXT (Texto)
- ODT (OpenOffice)
- PDFs com imagens apenas (digitalizados)

**Planned para próximas versões:**
- Suporte para DOCX
- Suporte para PDFs digitalizados (OCR)

### P: Um PDF com imagens funciona?
**R:** Não. O programa busca por texto. Se o PDF for digitalização:

**Solução:**
1. Use uma ferramenta OCR online
2. Converta para PDF com texto
3. Ou copie o texto de outro arquivo e salve como PDF

### P: O arquivo PDF tem que ter uma estrutura específica?
**R:** Não, qualquer PDF com texto funciona. Mas:

**Melhor compatibilidade:**
- PDFs criados digitalmente (não digitalizados)
- Estrutura clara: Contato, Resumo, Experiência, Formação, Habilidades
- Texto em português ou inglês

### P: Posso analisar currículos em outros idiomas?
**R:** Depende dos critérios. Se configurar palavras-chave em outro idioma, sim.

Exemplo para currículo em inglês:
```json
{
  "Habilidades Técnicas": {
    "palavras_chave": ["python", "javascript", "experience", "developer"]
  }
}
```

---

## Resultados e Relatórios

### P: Como salvar os resultados?
**R:** Atualmente não há botão "Salvar", mas pode:

1. **Copiar texto:** Ctrl+A na área de resultados, Ctrl+C, Ctrl+V em documento
2. **Tirar screenshot:**Prnt Scr → Colar em paint/documento
3. **Print direto:** Ctrl+P para imprimir
4. **Criar relatório:** Copie em Word/Google Docs com comentários pessoais

**Planned:** Exportar para PDF, Excel, JSON

### P: Como comparar vários candidatos?
**R:** 

**Opção 1 (Manual):**
- Analise cada um
- Anote a pontuação em um spreadsheet
- Compare lado a lado

**Opção 2 (Recomendado):**
```
Candidato | Pontuação | Exp | Tecn | Form | Cert | Idiom
João      | 75.5      | 90  | 85   | 80   | 50   | 60
Maria     | 82.3      | 95  | 90   | 75   | 70   | 75
Pedro     | 64.2      | 70  | 75   | 60   | 40   | 45
```

**Opção 3 (Futura):** Versão com análise em lote

### P: Posso exportar para Excel?
**R:** Não oficialmente, mas:

1. Copie os resultados
2. Cole em GitHub Copilot
3. Peça formatação em CSV
4. Importe no Excel

---

## Problemas Técnicos

### P: "Erro ao processar PDF"
**R:** Possíveis causas:

1. PDF corrompido
   - Solução: Tente com outro PDF
   
2. Permissões de leitura
   - Solução: Copie o PDF para outra pasta

3. Arquivo muito grande
   - Solução: Reduza/divida o PDF

4. Problema com caminho do arquivo
   - Solução: Use caminho sem caracteres especiais

### P: Aplicação fica lenta ou congela
**R:**

**Causas:**
- PDF muito grande (100+ MB)
- Computador sobrecarregado
- Muitos critérios

**Soluções:**
1. Feche outros programas
2. Reduza tamanho do PDF
3. Diminua número de critérios ativados
4. Reinicie o programa

### P: "Módulo não encontrado"
**R:** Dependência não instalada.

```bash
pip install PyPDF2
# Se não funcionar
pip install PyPDF2==3.0.1
```

### P: Janela não abre
**R:** 

**Windows:** Execute do CMD/PowerShell para ver erro:
```bash
python main.py
```

**Linux/Mac:**
```bash
python3 main.py
```

Se erro aparecer, procure a mensagem de erro aqui ou nos issues do GitHub.

---

## Desenvolvimento e Customização

### P: Posso modificar o código?
**R:** Sim! É open source. Você pode:
- Adicionar novos recursos
- Corrigir bugs
- Customizar para sua necessidade
- Melhorar interface

**Recomendação:** Faça backup antes de editar.

### P: Como adicionar suporte para DOCX?
**R:** Adicione ao `main.py`:

```python
from docx import Document

def extrair_texto_docx(caminho):
    doc = Document(caminho)
    texto = ""
    for paragrafo in doc.paragraphs:
        texto += paragrafo.text + "\n"
    return texto.lower()
```

### P: Como salvar análises em banco de dados?
**R:** Exemplo com SQLite:

```python
import sqlite3

def salvar_resultado(caminho_pdf, pontuacao, resultado_dict):
    conn = sqlite3.connect('avaliacoes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY,
            arquivo TEXT,
            pontuacao REAL,
            data TIMESTAMP
        )
    ''')
    cursor.execute('INSERT INTO avaliacoes VALUES (NULL, ?, ?, CURRENT_TIMESTAMP)',
                   (caminho_pdf, pontuacao))
    conn.commit()
    conn.close()
```

### P: Como usar machine learning para análise?
**R:** Veja próximas versões ou contribua!

Tecnologias recomendadas:
- Scikit-learn para classificação
- BERT para análise semântica
- Spacy para NLP

---

## Contribuição e Suporte

### P: Como reportar bugs?
**R:** 
1. Descreva o erro
2. Passo para reproduzir
3. Sistema operacional
4. Versão do Python

### P: Como sugerir melhorias?
**R:** 
- Abra uma "Issue" no GitHub
- Descreva a funcionalidade
- Dê exemplos de uso

### P: Posso contribuir com código?
**R:** Sim! Fork o projeto:
1. Clone o repositório
2. Faça suas mudanças
3. Teste bem
4. Envie Pull Request

---

## Roadmap - Próximas Versões

- [ ] Suporte para DOCX e TXT
- [ ] OCR para PDFs digitalizados
- [ ] Análise em lote de múltiplos currículos
- [ ] Exportação para PDF/Excel
- [ ] Banco de dados com histórico
- [ ] API REST
- [ ] Interface web (Flask/FastAPI)
- [ ] Machine Learning para análise semântica
- [ ] Integração com sistemas de RH

---

## Respostas Rápidas

| Pergunta | Resposta |
|----------|----------|
| **Funciona offline?** | Sim, 100% offline |
| **Precisa internet?** | Não |
| **Grátis?** | Sim |
| **Open source?** | Sim |
| **Risco de segurança?** | Nenhum, arquivos não são enviados |
| **Windows 7 suportado?** | Sim, se tiver Python 3.7+ |
| **Mac suportado?** | Sim |
| **Linux suportado?** | Sim |

---

**Não encontrou sua pergunta?** Procure documentação completa em `GUIA_COMPLETO.md` ou crie uma issue!

**Última atualização:** 10/03/2026
