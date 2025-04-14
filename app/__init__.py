from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Inicialização das extensões
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configurações básicas
    app.config.from_object("config.Config")

    # Inicialização das extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Registro de rotas
    from app.routes import product_routes
    app.register_blueprint(product_routes.bp)

    return app