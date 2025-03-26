# Desafio 2 - Livros VnW
Este projeto é uma API desenvolvida com Flask para cadastrar e listar livros doados, aplicando conceitos de desenvolvimento web, banco de dados e boas práticas na construção de APIs.

# Api Livros Doados VnW

Essa é uma API simples feita com Flask e SQLite para fins de estudo na escola Vai Na Web, ela permite cadastrar e listar os livros doados.

## Como rodar o projeto?

1. Faça o clone do repositório:
```bash
git clone https://github.com/Audreysilverio/Desafio2_LivrosVaiNaWeb.git
cd nome_do_projeto
```

2. Criar um ambiente virtual (Obrigatório):

**Windows**
```bash
python -m venv venv
source venv/Scripts/activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
python app.py
```

> A API estará disponível em http://127.0.0.1:5000/

## Endpoints

### POST /doar

Endpoint para cadastro das informações do livro doado.

**Envio (JSON)**
```json
{
    "titulo":"Ainda estou devendo o pix",
    "categoria":"Drama/Finanças",
    "autor":"Fernando Pilares",
    "image_url":"https://..."
}
```
**Resposta (201):**
```json
{
    "mensagem":"Livro cadastrado com sucesso!"
}
```

---

### GET /livros

O endpoint /livros retorna todos os livros cadastrados na API.

**Resposta (200):**
```json
{
    "id":"1",
    "titulo":"Ainda estou devendo o pix",
    "categoria":"Drama",
    "autor":"Fernando Pilares",
    "image_url":"https://..."
}
```
---

##  Tecnologias utilizadas

- Python 3
- Flask
- SQLite
- Flask-CORS

---

Feito por Audrey Silverio Ferreira para o programa Full Stack do VnW