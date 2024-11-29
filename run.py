# Importa a aplicação criada no módulo `__init__.py` e roda o servidor.
from app import create_app

# Cria a aplicação a partir da função `create_app`
app = create_app()

if __name__ == "__main__":
    # Roda a aplicação em modo de desenvolvimento
    app.run(debug=True)