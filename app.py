from flask import Flask, render_template, request
from agente import filtrar_refeicoes, gerar_resposta
import asyncio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        resultados = filtrar_refeicoes(pergunta)
        resposta = asyncio.run(gerar_resposta(pergunta, resultados))
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
