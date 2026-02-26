from flask import Flask
from .extensions import db, jwt
from .routes.auth_routes import auth
from .routes.produto_routes import produto_bp
from .routes.cliente_routes import cliente_bp
from .routes.venda_routes import venda_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(produto_bp, url_prefix="/produtos")
    app.register_blueprint(cliente_bp, url_prefix="/clientes")
    app.register_blueprint(venda_bp, url_prefix="/vendas")

    @app.route("/")
    def home():
        return {"status": "API Estoque Vendas Online"}

    return app