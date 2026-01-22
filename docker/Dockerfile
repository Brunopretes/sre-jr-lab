# 1. Usa uma imagem leve do Python
FROM python:3.12-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências para o container
COPY requirements.txt .

# 4. Instala as dependências (sem usar cache para diminuir a imagem)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o restante do código da pasta local para o container
COPY . .

# 6. Expõe a porta que a API vai usar
EXPOSE 8000

# 7. Comando para rodar a API (0.0.0.0 é obrigatório para rodar em container)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
