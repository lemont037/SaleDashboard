# 🚀 **Projeto Django com Docker e PostgreSQL** 🐳

Este repositório configura um ambiente Docker para uma aplicação Django com banco de dados PostgreSQL, da qual apresenta um Dashboard de Vendas. Aqui está como você pode facilmente rodar este projeto dentro de containers Docker.

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
   git clone https://github.com/lemont037/SaleDashboard.git
   cd SaleDashboard
   ```

2. Crie um arquivo `.env` com as variáveis de ambiente necessárias. Aqui você pode atribuir os valores que desejar:
   
   > *Informação:* Caso deseje, há um arquivo .env de exemplo, já configurado
   
   Template:

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
## 🚀 Documentação da API

A nossa API é completamente documentada utilizando o [Swagger UI](https://swagger.io/tools/swagger-ui/), permitindo que você visualize e interaja com os endpoints de forma simples e eficiente.

### 📝 Acessando a Documentação

Para acessar a documentação interativa da API, basta navegar até o seguinte endpoint em seu navegador:

```
http://localhost:8000/api/docs/
```

Esta interface exibe todos os endpoints da API, incluindo as descrições, parâmetros esperados e exemplos de resposta.

### 🔍 Exploração Interativa

O Swagger UI permite que você explore os recursos da API de forma interativa. Você pode:

- **Visualizar Endpoints**: Todos os endpoints disponíveis são listados, incluindo informações sobre os parâmetros de entrada e resposta.
- **Testar Endpoints**: Com um simples clique, você pode enviar requisições diretamente da interface do Swagger, facilitando os testes sem precisar de ferramentas externas como o Postman ou cURL.
- **Obter Exemplos de Respostas**: A documentação exibe exemplos de respostas que você pode esperar para cada requisição.

### ⚡ Funcionalidade de Pesquisa

Se você está buscando um endpoint específico, a interface permite realizar buscas rápidas. Basta digitar na barra de pesquisa e o Swagger UI filtrará os resultados para você.

### 📚 Descrição dos Endpoints

Aqui estão alguns dos principais endpoints disponíveis na API:

- **Criar um Canal de Vendas**:
  - **Método**: `POST`
  - **Endpoint**: `/create_salesChannel/<str:name>`
  - **Descrição**: Cria um novo canal de vendas. O parâmetro `name` é necessário para definir o nome do canal.

- **Listar Vendas**:
  - **Método**: `GET`
  - **Endpoint**: `/sales/`
  - **Descrição**: Retorna uma lista de vendas com a possibilidade de filtrar por `period_from`, `period_to`, `state` e `sale_channel`.

- **Criar uma Venda**:
  - **Método**: `POST`
  - **Endpoint**: `/sales/create/`
  - **Descrição**: Cria uma nova venda com base nos dados fornecidos no corpo da requisição.

### 🛠️ Atualizações Automáticas

Sempre que houver alterações na API, a documentação será atualizada automaticamente para refletir as novas mudanças. Não é necessário configurar nada adicionalmente para isso.

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
