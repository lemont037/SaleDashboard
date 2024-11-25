# Usar a imagem oficial do Python
FROM python:3.9

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências para dentro do container
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para dentro do container
COPY . /app/

# Expor a porta 8000
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]