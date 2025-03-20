import sqlite3  
from flask import Flask, request, jsonify  


app = Flask(__name__)


@app.route("/")
def bem_vindo():

    return "<h1>Espalhe conhecimento, doe um livro! 📚✨deac</h1>"


def init_db():
    with sqlite3.connect("database.db") as conn:

        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,  
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,  
                    image_url TEXT NOT NULL 
                )
            """
        )  


init_db()


@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()
    print(f" AQUI ESTÃO OS DADOS RETORNADOS DO CLIENTE {dados}")  

    titulo = dados.get("titulo")  
    categoria = dados.get("categoria")  
    autor = dados.get("autor")  
    image_url = dados.get("image_url")  

    
    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400  
    
    
    with sqlite3.connect("database.db") as conn:
    
        conn.execute(f"""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)
    
    conn.commit()  
    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

if __name__ == "__main__":
   
    app.run(debug=True)