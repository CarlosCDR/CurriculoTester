# 🌐 Versão Web - Avaliador de Currículos

Interface web moderna para avaliação inteligente de currículos em PDF.

## 🚀 Início Rápido

### 1. Instalar
```bash
# Windows
instalar_web.bat

# Linux/Mac
chmod +x instalar_web.sh && ./instalar_web.sh

# Manual
pip install -r requirements_web.txt
```

### 2. Executar
```bash
# Fácil
python executar_web.py

# Direto
python app_web.py
```

### 3. Acessar
Abra seu navegador em: **http://localhost:5000**

## 🎨 Interface Web

### ✨ Funcionalidades
- ✅ **Upload Drag & Drop** - Arraste arquivos PDF
- ✅ **Interface Moderna** - Bootstrap 5 + Design Responsivo
- ✅ **Análise Visual** - Gráficos e barras de progresso
- ✅ **Resultados Detalhados** - Pontos positivos/negativos
- ✅ **Compartilhamento** - Links para resultados
- ✅ **Mobile Friendly** - Funciona em smartphones

### 📱 Páginas Disponíveis

| Página | Descrição | URL |
|--------|-----------|-----|
| **Início** | Upload e análise | `/` |
| **Resultado** | Análise detalhada | `/analisar` |
| **Configuração** | Critérios avançados | `/configuracao` |
| **Ajuda** | FAQ e guias | `/ajuda` |
| **Sobre** | Informações | `/sobre` |

## 🛠️ Arquitetura Web

```
app_web.py (Flask App)
├── templates/          # HTML Templates
│   ├── base.html      # Layout base
│   ├── index.html     # Página inicial
│   ├── resultado.html # Resultados
│   ├── configuracao.html
│   ├── ajuda.html
│   ├── sobre.html
│   ├── 404.html
│   └── 500.html
├── static/            # CSS/JS/Images (futuro)
└── requirements_web.txt
```

## 🔧 API Endpoints

### Análise via Form
```http
POST /analisar
Content-Type: multipart/form-data

curriculo: <arquivo PDF>
criterio_*: on/off (para cada critério)
```

### API JSON (Futuro)
```http
POST /api/analisar
Content-Type: multipart/form-data

file: <arquivo PDF>
criterios: ["Experiência", "Habilidades"]
```

## 🎯 Diferenças da Versão Desktop

| Aspecto | Desktop | Web |
|---------|---------|-----|
| **Interface** | Tkinter (básica) | Bootstrap (moderna) |
| **Compartilhamento** | Manual | Links diretos |
| **Acesso** | Local apenas | Rede local possível |
| **Mobile** | ❌ | ✅ |
| **Instalação** | Executável único | Dependências Python |
| **Tamanho** | ~50MB | ~10MB |

## 🌐 Deploy em Produção

### Opções de Deploy

#### 1. **Local (Recomendado)**
```bash
python executar_web.py
# Acesse: http://localhost:5000
```

#### 2. **Docker (Futuro)**
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements_web.txt
EXPOSE 5000
CMD ["python", "app_web.py"]
```

#### 3. **Servidor Local**
```bash
# Para rede local
python app_web.py  # host='0.0.0.0'
# Acesse: http://IP_DO_SERVIDOR:5000
```

### ⚠️ Avisos de Segurança

- **Não exponha publicamente** sem autenticação
- **Use HTTPS** em produção
- **Configure firewall** apropriadamente
- **Monitore logs** de acesso

## 📊 Comparação de Versões

| Versão | Interface | Instalação | Uso | Compartilhamento |
|--------|-----------|------------|-----|------------------|
| **Desktop** | Tkinter | Executável | Individual | Manual |
| **Web** | Bootstrap | Python deps | Equipe | Links |

## 🚀 Próximos Passos

### Melhorias Planejadas
- [ ] Autenticação de usuários
- [ ] Histórico de análises
- [ ] Dashboard com estatísticas
- [ ] API REST completa
- [ ] Deploy em nuvem
- [ ] Temas customizáveis
- [ ] Export PDF dos resultados

### Como Contribuir
1. Fork o projeto
2. Crie branch: `git checkout -b feature/web-improvements`
3. Modifique templates em `templates/`
4. Teste: `python executar_web.py`
5. Pull Request

## 📞 Suporte

### Problemas Comuns

**"Template não encontrado"**
```bash
# Verificar se templates existem
ls templates/
# Instalar dependências
pip install -r requirements_web.txt
```

**"Porta já em uso"**
```python
# Mudar porta em app_web.py
app.run(port=8000)  # ou outra porta
```

**"Erro de upload"**
- Verificar tamanho do arquivo (< 16MB)
- Confirmar que é PDF válido
- Verificar permissões de escrita

---

## 🎉 Conclusão

A versão web oferece uma experiência moderna e compartilhável para análise de currículos, mantendo toda a inteligência da versão desktop com uma interface mais amigável.

**Experimente agora:**
```bash
python executar_web.py
```

Acesse: http://localhost:5000

---

**Versão:** 1.0-web  
**Última atualização:** 2026-03-11  
**Status:** ✅ Pronto para uso
