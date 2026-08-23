from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, jwt, ma, migrate

# Import models so SQLAlchemy registers them
from models.merchants import Merchant
from models.store import Store
from models.store_admin import StoreAdmin

# Import your blueprints
from routes.merchants_routes import merchants_bp
from routes.store_routes import store_bp
from routes.store_admin_routes import store_admin_bp


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)

    # Extensions
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # CORS
    CORS(app)

    # Register your blueprints
    app.register_blueprint(merchants_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(store_admin_bp)

    @app.route("/")
    def home():
        return {
            "message": "MyDuka Backend API is running"
        }, 200

    @app.route("/health")
    def health():
        return {
            "status": "healthy"
        }, 200

    return app


app = create_app()
