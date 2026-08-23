from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import user
from extensions import db

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    
    if not name or not password:
        return jsonify({'message': 'Name and password are required'}), 400
    
    use = user.query.filter_by(name=name).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid name or password'}), 401
    
    access_token = create_access_token(identity=user.user_id)
    return jsonify({
        'access_token': access_token,
        'user_id': user.user_id,
        'name': user.name,
        'role': user.role
    }), 200