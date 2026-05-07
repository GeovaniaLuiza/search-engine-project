# Imagem base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expor porta
EXPOSE 8000

# Rodar aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]