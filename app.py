from flask import Flask
from config import Config
from controllers import register_routes
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)

# Habilitar CORS para todas las rutas
CORS(app)

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
