# Importa o Flask para criar a aplicação
from flask import Flask

def create_app():
    """Função para criar e configurar a aplicação Flask."""
    app = Flask(__name__)

    # Configurações da aplicação (como a chave da API OpenAI)
    app.config.from_pyfile('../config.py')

    # Importa e registra as rotas
    from .routes import main
    app.register_blueprint(main)

    return app