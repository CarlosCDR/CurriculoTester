# 🏗️ Arquitetura Técnica - Avaliador de Currículos

## Visão Geral da Arquitetura

```
┌────────────────────────────────────────────────────────┐
│                   Interface Gráfica (Tkinter)          │
│              InterfaceAvaliador (classe)               │
└────────────────────┬─────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
    Carregar    Configurar   Analisar
    PDF         Critérios    Currículo
        │            │            │
        └────────────┼────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
   Processos   Critérios  Análise
   (PDF)       (JSON)     (engine)
```

## Componentes Principais

### 1. `CriterioCurriculo`
**Responsabilidade:** Definir e gerenciar critérios de avaliação

```python
class CriterioCurriculo:
    CRITERIOS_PREDEFINIDOS = {
        "Critério": {
            "descricao": str,        # Descrição amigável
            "peso": int,             # 0-100, importância relativa
            "palavras_chave": list,  # O que buscar no currículo
            "tipo": str             # numerico, categorico, lista
        }
    }
```

**Atributos principais:**
- `descricao`: Explica o que o critério avalia
- `peso`: Define a importância (soma ≈ 100)
- `palavras_chave`: Como o critério é detectado
- `tipo`: Afeta como a pontuação é calculada

**Exemplo:**
```python
"Experiência": {
    "descricao": "Anos de experiência na área",
    "peso": 25,
    "palavras_chave": ["experiência", "anos", "trabalho"],
    "tipo": "numerico"
}
```

### 2. `ProcessadorPDF`
**Responsabilidade:** Extrair texto de arquivos PDF

```python
class ProcessadorPDF:
    @staticmethod
    def extrair_texto(caminho_pdf) -> str
```

**Como funciona:**
1. Abre arquivo PDF
2. Itera por todas as páginas
3. Extrai texto de cada página
4. Concatena tudo em uma string
5. Converte para minúsculas (case-insensitive)

**Dependência:** PyPDF2

**Tratamento de erros:**
- PDF corrompido → Retorna mensagem de erro
- Arquivo não encontrado → Retorna mensagem de erro
- PyPDF2 não instalado → Mensagem clara

### 3. `AnalisadorCurriculo`
**Responsabilidade:** Analisar currículo e gerar pontuação

```python
class AnalisadorCurriculo:
    def __init__(self, criterios_customizados=None)
    def analisar(self, texto, criterios_ativos) -> dict
    def _gerar_recomendacoes(self, resultado, texto) -> list
```

**Fluxo de análise:**

```
Entrada: Texto do currículo + Critérios ativos
    ↓
Para cada critério:
    ↓
    Contar correspondências de palavras-chave
    ↓
    Calcular pontuação: (matches / total_keywords) * 100
    ↓
    Multiplicar pelo peso
    ↓
Somar todas as pontuações ponderadas
    ↓
Normalizar pelo peso total
    ↓
Gerar recomendações baseado na pontuação final
    ↓
Retorna: {
    "pontuacao_total": float,
    "pontos_positivos": list,
    "pontos_negativos": list,
    "detalhes_criterios": dict,
    "recomendacoes": list
}
```

**Fórmula de Pontuação:**

$$\text{Pontuação Final} = \frac{\sum_{i=1}^{n} (\text{Pontuação}_i \times \text{Peso}_i)}{\sum_{i=1}^{n} \text{Peso}_i}$$

Onde:
- $\text{Pontuação}_i$ = (correspondências encontradas / total de palavras-chave) × 100
- $\text{Peso}_i$ = peso do critério i

**Exemplo:**
```
Critério: Habilidades Técnicas
Palavras-chave: ["python", "javascript", "java", "sql", "react"]
Encontradas: ["python", "react", "java"]

Pontuação = (3 / 5) * 100 = 60%
Com peso 30%: 60 × 0.30 = 18 pontos
```

### 4. `InterfaceAvaliador`
**Responsabilidade:** Gerenciar interface gráfica com Tkinter

```python
class InterfaceAvaliador:
    def __init__(self, janela)
    def _criar_interface()
    def _carregar_pdf()
    def _analisar()
    def _exibir_resultados(resultado)
    def _limpar()
```

**Estrutura da Interface:**

```
┌─ Frame Arquivo ──────────────────────┐
│ [Nenhum arquivo] [Carregar PDF]      │
└──────────────────────────────────────┘

┌─ Frame Critérios ────────────────────┐
│ ☑ Experiência         (Peso: 25%)   │
│ ☑ Formação            (Peso: 20%)   │
│ ☑ Habilidades Técnicas(Peso: 30%)   │
│ ☑ Certificações       (Peso: 15%)   │
│ ☑ Idiomas             (Peso: 10%)   │
└──────────────────────────────────────┘

┌─ Frame Botões ───────────────────────┐
│ [Analisar] [Limpar]                  │
└──────────────────────────────────────┘

┌─ Frame Resultados ───────────────────┐
│                                      │
│ (Texto com resultado scrollável)     │
│                                      │
└──────────────────────────────────────┘
```

**Widgets principais:**
- `ttk.LabelFrame`: Agrupa seções
- `ttk.Checkbutton`: Ativa/desativa critérios
- `tk.Text`: Exibe resultados
- `ttk.Button`: Ações (carregar, analisar, limpar)

---

## Fluxo de Dados

### Fluxo 1: Carregar PDF
```
Clique [Carregar PDF]
    ↓
filedialog.askopenfilename()
    ↓
Usuário seleciona arquivo
    ↓
Armazenar em self.file_path
    ↓
Atualizar label com nome do arquivo
```

### Fluxo 2: Configurar Critérios
```
Usuário marca/desmarcar ☑
    ↓
BooleanVar atualiza automaticamente
    ↓
Valor armazenado no dicionário self.vars_criterios
```

### Fluxo 3: Analisar
```
Clique [Analisar Currículo]
    ↓
Validar se arquivo foi selecionado
    ↓
ProcessadorPDF.extrair_texto(self.file_path)
    ↓
Obter critérios selecionados do dicionário
    ↓
AnalisadorCurriculo.analisar(texto, criterios)
    ↓
Formatar resultado de forma legível
    ↓
_exibir_resultados(resultado)
    ↓
Inserir texto no widget Text
```

---

## Estrutura de Dados Chave

### Resultado da Análise
```json
{
  "pontos_positivos": [
    "✓ Experiência: Encontradas 8 correspondências",
    "✓ Habilidades Técnicas: Encontradas 5 correspondências"
  ],
  "pontos_negativos": [
    "✗ Idiomas: Apenas 1 correspondência encontrada"
  ],
  "pontuacao_total": 72.5,
  "detalhes_criterios": {
    "Experiência": {
      "pontuacao": 85.0,
      "peso": 25,
      "correspondencias": 8
    },
    "Habilidades Técnicas": {
      "pontuacao": 75.0,
      "peso": 30,
      "correspondencias": 5
    }
  },
  "recomendacoes": [
    "ℹ️ Currículo com compatibilidade moderada",
    "📝 Considere destacar mais as habilidades"
  ]
}
```

### Critério no JSON
```json
{
  "Experiência": {
    "descricao": "Anos de experiência na área",
    "peso": 25,
    "palavras_chave": ["experiência", "anos", "trabalho"],
    "tipo": "numerico"
  }
}
```

---

## Dependências Externas

| Biblioteca | Versão | Uso |
|-----------|--------|-----|
| PyPDF2 | 3.0.1 | Extrair texto de PDFs |
| tkinter | builtin | Interface gráfica |
| json | builtin | Ler configurações |
| re | builtin | Expressões regulares |
| os | builtin | Operações de arquivo |
| datetime | builtin | Data/hora |

---

## Padrões de Design Utilizados

### 1. **Separação de Responsabilidades**
- Cada classe tem uma responsabilidade única
- ProcessadorPDF: Apenas PDF
- AnalisadorCurriculo: Apenas análise
- InterfaceAvaliador: Apenas UI

### 2. **Model-View Pattern**
- Model: CriterioCurriculo, ProcessadorPDF, AnalisadorCurriculo
- View: InterfaceAvaliador

### 3. **Dependency Injection**
```python
class AnalisadorCurriculo:
    def __init__(self, criterios_customizados=None):
        # Permite passar critérios personalizados
        self.criterios = criterios_customizados or DEFAULT
```

### 4. **Static Methods**
```python
class ProcessadorPDF:
    @staticmethod
    def extrair_texto(caminho):
        # Não precisa de instância
```

---

## Pontos de Extensão

### 1. Adicionar Novo Tipo de Critério
**Arquivo:** `main.py` → `CriterioCurriculo.CRITERIOS_PREDEFINIDOS`

```python
"Novo Tipo": {
    "descricao": "descrição",
    "peso": 20,
    "palavras_chave": ["palavra1", "palavra2"],
    "tipo": "novo_tipo"
}
```

### 2. Adicionar Novo Formato de Arquivo
**Arquivo:** `main.py` → `ProcessadorPDF`

```python
@staticmethod
def extrair_texto_docx(caminho):
    from docx import Document
    # implementação
    
@staticmethod
def extrair_texto(caminho):
    if caminho.endswith('.docx'):
        return ProcessadorPDF.extrair_texto_docx(caminho)
    elif caminho.endswith('.pdf'):
        return ProcessadorPDF.extrair_texto_pdf(caminho)
```

### 3. Adicionar Machine Learning
**Implementação futura:**

```python
class AnalisadorCurriculoML(AnalisadorCurriculo):
    def __init__(self, modelo_ml):
        super().__init__()
        self.modelo = modelo_ml
    
    def analisar(self, texto, criterios_ativos):
        # Usar modelo para análise semântica
        # Combinar com análise por palavras-chave
```

### 4. Adicionar Persistência
**Implementação futura:**

```python
class GerenciadorResultados:
    def salvar_resultado(self, arquivo, resultado):
        # Salvar em banco de dados
        pass
    
    def listar_resultados(self):
        # Recuperar histórico
        pass
```

---

## Performance

### Análise de Complexidade

| Operação | Complexidade | Tempo Típico |
|----------|-------------|--------------|
| Extrair texto PDF (10 pág) | O(n) | 0.5-2s |
| Análise (5 critérios) | O(m × k) | 0.1-0.5s |
| Renderizar resultado | O(r) | 0.05-0.1s |

Onde:
- n = tamanho do PDF
- m = número de critérios
- k = média de palavras-chave
- r = linhas de resultado

### Otimizações Possíveis

1. **Cache de PDFs processados**
   ```python
   self.cache_pdfs = {}
   if caminho in self.cache_pdfs:
       return self.cache_pdfs[caminho]
   ```

2. **Processamento assíncrono**
   ```python
   import threading
   thread = threading.Thread(target=self._analisar_async)
   ```

3. **Compilar regex para palavras-chave**
   ```python
   import re
   pattern = re.compile('|'.join(palavras_chave))
   matches = pattern.findall(texto)
   ```

---

## Testes Sugeridos

### Testes Unitários
```python
def test_procesador_pdf():
    texto = ProcessadorPDF.extrair_texto('test.pdf')
    assert isinstance(texto, str)
    assert len(texto) > 0

def test_analisador_pontuacao():
    resultado = analisador.analisar("python django", ["python"])
    assert 50 <= resultado["pontuacao_total"] <= 100
```

### Testes de Integração
```python
def test_fluxo_completo():
    # 1. Carregar PDF
    # 2. Configurar critérios
    # 3. Analisar
    # 4. Verificar resultado
```

### Testes de Performance
```python
import time
start = time.time()
ProcessadorPDF.extrair_texto('large.pdf')
assert time.time() - start < 5  # Máximo 5 segundos
```

---

## Segurança

### Considerações

1. **Arquivo Local:** Nenhum arquivo é enviado para servidores
2. **Entrada Validada:** Apenas arquivos PDF são processados
3. **Sem Dependências Perigosas:** PyPDF2 é biblioteca confiável
4. **Sem Acesso à Rede:** Aplicação completamente offline

### Melhorias Futuras

1. Validar estrutura do PDF antes de processar
2. Limpar memória após análise
3. Criptografar resultados se necessário
4. Auditoria de acesso a arquivos

---

## Troubleshooting Técnico

### Debug Mode
```python
# Adicione ao início do main.py
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

### Verificar Extração de Texto
```python
# No prompt interativo
from main import ProcessadorPDF
texto = ProcessadorPDF.extrair_texto('seu_arquivo.pdf')
print(len(texto), "caracteres")
print(texto[:500])  # Primeiros 500 chars
```

### Simulação de Análise
```python
from main import AnalisadorCurriculo
analisador = AnalisadorCurriculo()
resultado = analisador.analisar("python django", ["python"])
print(resultado)
```

---

## Roadmap Técnico

### v1.0 (Atual)
- [x] Processamento de PDF
- [x] Análise por palavras-chave
- [x] Interface básica
- [x] Critérios customizáveis

### v1.1
- [ ] Suporte for DOCX
- [ ] Suporte para TXT
- [ ] Análise em lote
- [ ] Exportar resultados

### v2.0
- [ ] Banco de dados
- [ ] API REST
- [ ] Interface web
- [ ] Machine Learning

### v3.0
- [ ] Integração com HRIS
- [ ] Análise de vídeo entrevista
- [ ] Ranking automático de candidatos
- [ ] Relatórios avançados

---

**Última atualização:** 10/03/2026
**Versão da Documentação:** 1.0
