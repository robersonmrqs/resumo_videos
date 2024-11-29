# Importa os módulos do Flask necessários
from flask import Blueprint, render_template, request, jsonify
# Importa a função de extração de áudio
from .services import download_audio_from_video

# Cria um blueprint para as rotas principais
main = Blueprint("main", __name__)

# Rota para a página inicial
@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recebe a URL do vídeo enviada pelo formulário
        video_url = request.form.get("video_url")
        
        try:
            # Baixa e extrai o áudio do vídeo
            audio_path = download_audio_from_video(video_url)
            # Retorna o caminho do áudio para o front-end (a ser exibido no HTML)
            return jsonify({"message": "Áudio extraído com sucesso!", "audio_path": audio_path})

        except Exception as e:
            return jsonify({"error": str(e)})

    # Renderiza a página inicial
    return render_template("index.html")