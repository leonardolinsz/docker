# Imagem base Python
FROM python:3.12-slim

# Definindo variaveis de ambiente para o banco
ENV MYSQL_HOST=db
ENV MYSQL_USER=appuser
ENV MYSQL_PASSWORD=senha123
ENV MYSQL_DATABASE=appdb

# Diretório de trabalho
WORKDIR /app

# Copiando os arquivos de requisitos
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Volume para logs

VOLUME /app/logs

# Comando de execução

CMD ["python"]