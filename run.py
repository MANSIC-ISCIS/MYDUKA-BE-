from flask import Flask
from db import db
from routes.products_routes import products_bp
from routes.suppliers_routes import suppliers_bp
from routes.supply_req_routes import supply_req_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myduka.db'

db.init_app(app)

# Register Blueprints
app.register_blueprint(products_bp, url_prefix='/api')
app.register_blueprint(suppliers_bp, url_prefix='/api')
app.register_blueprint(supply_req_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5000)