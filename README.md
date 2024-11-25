# 🚀 **Projeto Django com Docker e PostgreSQL** 🐳

Este repositório configura um ambiente Docker para uma aplicação Django com banco de dados PostgreSQL. Aqui está como você pode facilmente rodar este projeto dentro de containers Docker.

---

## 🧑‍💻 **Tecnologias Utilizadas**

- **Django** 🐍
- **PostgreSQL** 🗃️
- **Docker** 🐳
- **Docker Compose** ⚙️

---

## 🚧 **Pré-requisitos**

Antes de começar, você precisa ter o seguinte instalado:

- [Docker](https://www.docker.com/get-started) 🐳
- [Docker Compose](https://docs.docker.com/compose/install/) ⚙️

---

## 🏗️ **Como Rodar o Projeto**

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/projeto-django-docker.git
   cd projeto-django-docker
   ```

2. Crie um arquivo `.env` com as variáveis de ambiente necessárias. Aqui você pode atribuir os valores que desejar:
   
   > *Informação:* Caso deseje, há um arquivo .env de exemplo, já configurado
   
   Exemplo:

   ```bash
    SECRET_KEY=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    DB_HOST=
   ```

3. Execute o comando abaixo para rodar os containers:

   ```bash
   docker-compose up --build
   ```

4. Acesse a aplicação no navegador:

   [http://localhost:8000](http://localhost:8000) 🌐

---
## 🔍 **Uso dos Filtros**
Essa é uma lista dos registros criados por padrão no banco, por meio dessas informações é fácil testar os filtros na interface:

|Data|Preço|Custo|Estado|Canal de venda|
|----|-----|-----|------|--------------|
|24/01/2024 12:45:30|150.00|45.50|CE|marketplace|
|26/07/2024 09:38:01|259.99|75.01|CE|loja|
|08/09/2024 00:00:15|781.00|600.00|SP|loja|
|15/09/2024 16:00:59|45.00|9.00|RJ|marketplace|
|30/09/2024 07:30:34|1150.00|900.00|RJ|marketplace|
|30/09/2024 12:23:35|9.99|9.00|BA|loja|

---

## 🧑‍💻 **Scripts Importantes**

- **Executar migrações do banco de dados**:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

- **Criar um superusuário para o Django**:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

- **Acessar o shell do Django**:

   ```bash
   docker-compose exec web python manage.py shell
   ```
---

## 💬 **Contato**

- **Email**: leonardomm037@gmail.com 📧
- **GitHub**: [@lemont037](https://github.com/lemont037) 🐱

---

### 🌟 **Aproveite o desenvolvimento!**
