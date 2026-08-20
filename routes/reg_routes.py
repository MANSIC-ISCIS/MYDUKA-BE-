from flask import Blueprint, request, jsonify

from extensions import db
from models.user import user
from models.invitation import Invitation

reg_bp = Blueprint("reg", __name__, url_prefix="/auth")


@reg_bp.route("/register-merchant", methods=["POST"])
def register_merchant():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    #check required fields
    if not name or not email or not password:
        return jsonify({
            "error": "Name, email and password are required"
        }), 400

    existing_user = user.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "error": "Email already registered"
        }), 409

    merchant = user(
        name=name,
        email=email,
        role="merchant"
    )

    merchant.set_password(password)

    db.session.add(merchant)
    db.session.commit()

    return jsonify({
        "message": "Merchant registered successfully"
    }), 201
