# 🔎 Motor de Busca em Documentos

Sistema de busca em arquivos de texto utilizando diferentes algoritmos clássicos de substring search, com observabilidade completa (OpenTelemetry + Prometheus + Grafana).

---

## 📌 Descrição

Este projeto implementa um motor de busca que permite ao usuário pesquisar palavras ou trechos dentro de arquivos `.txt`, escolhendo em tempo de execução o algoritmo de busca.

Além da busca, o sistema coleta métricas e traces para análise de performance entre algoritmos.

---

## 🧠 Algoritmos implementados

- 🔹 Força Bruta (Naive)
- 🔹 KMP (Knuth-Morris-Pratt)
- 🔹 Rabin-Karp
---

## 🎯 Funcionalidades

- 📂 Upload de arquivos `.txt`
- 🔎 Busca de padrões em texto
- ⚙️ Seleção de algoritmo em tempo de execução
- 📍 Retorno de posições encontradas
- 📊 Contagem de ocorrências
- ⏱️ Medição de tempo de execução (ms)
- 📈 Métricas com Prometheus
- 🔭 Tracing com OpenTelemetry
- 📊 Dashboard no Grafana

---

## 🛠️ Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn
- OpenTelemetry
- Prometheus
- Grafana
- HTML + JavaScript

---

## 📁 Estrutura do projeto

```bash
search-engine-project/
│
├── app/
│ ├── main.py
│ ├── strategies/
│ │ ├── naive.py
│ │ ├── kmp.py
│ │ ├── rabin_karp.py
│ │ └── boyer_moore.py
│ ├── metrics.py
│ └── telemetry.py
├── documents/
│ ├── bible.txt
│ ├── cathedral_bazaar.txt
│ ├── dom_casmurro.txt
│ ├── os_lusiadas.txt
├── frontend/
│ └── index.html
├── prometheus.yml
├── docker-compose.yml
└── README.md

```

## ⚙️ Instalação

### 1. Clonar

```bash
git clone https://github.com/seu-usuario/search-engine-project.git
cd search-engine-project
2. Criar ambiente virtual
python -m venv venv

Ativar:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
🚀 Execução
▶️ Rodar a API
python -m uvicorn app.main:app --reload

A API ficará disponível em:

http://localhost:8000

📌 Documentação Swagger:

http://localhost:8000/docs
🌐 Rodar o frontend

Abra o arquivo:

frontend/index.html

Ou use Live Server no VS Code.

📊 Métricas (Prometheus)

Endpoint de métricas:

http://localhost:8000/metrics
Métricas disponíveis:
search_requests_total
search_duration_ms
document_size_chars
