import math

from flask import Flask, flash, redirect, render_template, request, session, url_for

import database

app = Flask(__name__)

database.criar_banco()

@app.route("/")
def index():
    treinos = database.listar_treinos()
    return render_template("index.html", treinos=treinos)


@app.route("/treinos/novo", methods=["GET", "POST"])
def novo_treino():
    if request.method == "POST":
        titulo = request.form["titulo"]
        tipo = request.form["tipo"]
        duracao = int(request.form["duracao"])
        database.criar_treino(titulo, tipo, duracao)
        flash("Treino cadastrado.")
        return redirect(url_for("index"))

    return render_template("novo_treino.html")


@app.route("/treinos/<int:treino_id>/editar", methods=["GET", "POST"])
def editar_treino(treino_id):
    treino = database.buscar_treino(treino_id)
    if treino is None:
        return "Treino não encontrado", 404

    if request.method == "POST":
        titulo = request.form["titulo"]
        tipo = request.form["tipo"]
        duracao = int(request.form["duracao"])
        database.atualizar_treino(treino_id, titulo, tipo, duracao)
        flash("Treino atualizado.")
        return redirect(url_for("index"))

    return render_template("editar_treino.html", treino=treino)


@app.post("/treinos/<int:treino_id>/concluir")
def concluir_treino(treino_id):
    database.alternar_concluido(treino_id)
    flash("Status do treino atualizado.")
    return redirect(url_for("index"))


@app.post("/treinos/<int:treino_id>/excluir")
def excluir_treino(treino_id):
    database.excluir_treino(treino_id)
    flash("Treino excluído.")
    return redirect(url_for("index"))


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("registro"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Implemente o login com session.")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
