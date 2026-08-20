from flask import Flask, jsonify
from flask_cors import CORS

from extensions import db, jwt
from config import Config

from routes.auth_routes import auth_bp
from routes.merchants_routes import merchant_bp
from routes.store_admin_routes import admin_bp
from routes.clerks_routes import clerk_bp
from routes.products_routes import product_bp
from routes.payment_routes import payment_bp
from routes.records_routes import records_bp
from routes.store_routes import store_bp

app = Flask(__name__)

app.config.from_object(Config)

# =========================================================
# INITIALIZE EXTENSIONS
# =========================================================

db.init_app(app)
jwt.init_app(app)

CORS(app, origins="*", supports_credentials=True)


# =========================================================
# REGISTER BLUEPRINTS
# =========================================================

app.register_blueprint(auth_bp)
app.register_blueprint(merchant_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(clerk_bp)
app.register_blueprint(product_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(records_bp)
app.register_blueprint(store_bp)

@app.route("/")
def home():

    return jsonify({
        "message": "MyDuka API is running"
    })


if __name__ == "__main__":
    app.run(debug=True)
