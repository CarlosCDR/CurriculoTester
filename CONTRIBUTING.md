# 🤝 Guia de Contribuição

Obrigado pelo interesse em contribuir com o **Avaliador de Currículos**! Este documento explica como participar do projeto.

---

## 📋 Índice

- [Como Contribuir](#como-contribuir)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Fluxo de Trabalho](#fluxo-de-trabalho)
- [Padrões de Código](#padrões-de-código)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Features](#sugerindo-features)

---

## Como Contribuir

Contribuições de qualquer tamanho são bem-vindas:

- 🐛 **Correção de bugs** – abra uma issue ou envie um PR diretamente
- ✨ **Novas features** – discuta a ideia em uma issue antes de implementar
- 📖 **Documentação** – melhorias em READMEs, comentários ou docstrings
- 🧪 **Testes** – adicione ou melhore testes existentes
- 🌐 **Tradução** – ajude a internacionalizar o projeto

---

## Configuração do Ambiente

```bash
# 1. Fork e clone o repositório
git clone https://github.com/YOUR-USERNAME/CurriculoTester.git
cd CurriculoTester

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Instale as dependências de desenvolvimento
pip install -r requirements.txt
pip install -r requirements_web.txt

# 4. Verifique a instalação
python testar_instalacao.py
```

---

## Fluxo de Trabalho

```bash
# 1. Sincronize com o repositório original
git remote add upstream https://github.com/CarlosCDR/CurriculoTester.git
git fetch upstream
git checkout main
git merge upstream/main

# 2. Crie uma branch descritiva
git checkout -b feature/suporte-docx
# ou
git checkout -b fix/corrige-pontuacao-criterios

# 3. Faça suas alterações e adicione testes

# 4. Commit com mensagem clara (seguindo Conventional Commits)
git commit -m "feat: adiciona suporte para arquivos DOCX"
git commit -m "fix: corrige cálculo de pontuação quando critério tem peso zero"
git commit -m "docs: atualiza README com exemplo da API REST"

# 5. Push e abra um Pull Request
git push origin feature/suporte-docx
```

---

## Padrões de Código

### Python

- Siga o **PEP 8** para formatação
- Use **docstrings** em todas as classes e métodos públicos
- Nomes de variáveis e funções em português (consistente com o projeto)
- Nomes de classes em PascalCase

```python
class MeuProcessador:
    """Descrição clara da responsabilidade da classe."""

    def processar(self, texto: str) -> dict:
        """
        Processa o texto fornecido.

        Args:
            texto: Texto a ser processado.

        Returns:
            Dicionário com os resultados do processamento.
        """
        ...
```

### Commits (Conventional Commits)

| Prefixo | Uso |
|---------|-----|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Alterações na documentação |
| `refactor:` | Refatoração sem mudança de comportamento |
| `test:` | Adição ou correção de testes |
| `chore:` | Tarefas de manutenção (CI, dependências) |

---

## Reportando Bugs

Ao abrir uma issue de bug, inclua:

1. **Descrição** – O que acontece vs. o que deveria acontecer
2. **Passos para reproduzir** – Sequência exata de ações
3. **Ambiente** – Sistema operacional, versão do Python, versão das dependências
4. **Logs ou screenshots** – Qualquer saída de erro relevante

**Template:**

```
**Descrição do bug:**
Ao analisar um PDF com caracteres especiais, a pontuação retorna 0.

**Passos para reproduzir:**
1. Execute `python main.py`
2. Carregue `curriculo_especial.pdf`
3. Clique em "Analisar Currículo"

**Comportamento esperado:**
A pontuação deveria ser calculada normalmente.

**Ambiente:**
- OS: Windows 11
- Python: 3.11.2
- PyPDF2: 3.0.1
```

---

## Sugerindo Features

Antes de implementar uma nova feature, abra uma issue descrevendo:

- **Motivação** – Qual problema ela resolve?
- **Proposta** – Como ela funcionaria?
- **Alternativas** – Outras abordagens consideradas?

---

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto.
