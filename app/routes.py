# Importa os módulos do Flask necessários
from flask import Blueprint, render_template, request, jsonify

# Cria um blueprint para as rotas principais
main = Blueprint("main", __name__)

# Rota para a página inicial
@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recebe a URL do vídeo enviada pelo formulário
        video_url = request.form.get("video_url")
        # Aqui faremos o processamento (a ser implementado)
        return jsonify({"message": "URL recebida", "url": video_url})

    # Renderiza a página inicial
    return render_template("index.html")