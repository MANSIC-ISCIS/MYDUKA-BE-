from flask import Blueprint, request, jsonify
from extensions import db
from models.merchants import Merchant
from schemas.merchant_schema import merchant_schema, merchants_schema

merchants_bp = Blueprint("merchants", __name__, url_prefix="/api/merchants")

@merchants_bp.route("/<int:merchant_id>", methods=["GET"])
def get_merchant(merchant_id):
    merchant = Merchant.query.get(merchant_id)

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    return jsonify({
        "merchant": merchant_schema.dump(merchant)
    }), 200


@merchants_bp.route("/<int:merchant_id>", methods=["PUT"])
def update_merchant(merchant_id):
    merchant = Merchant.query.get(merchant_id)

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "merchant_name" in data:
        merchant.merchant_name = data["merchant_name"]

    if "email" in data:
        existing_merchant = Merchant.query.filter(
            Merchant.email == data["email"],
            Merchant.merchant_id != merchant_id
        ).first()

        if existing_merchant:
            return jsonify({
                "error": "A merchant with this email already exists"
            }), 409

        merchant.email = data["email"]

    if "password" in data:
        merchant.password = data["password"]

    db.session.commit()

    return jsonify({
        "message": "Merchant updated successfully",
        "merchant": merchant_schema.dump(merchant)
    }), 200


@merchants_bp.route("/<int:merchant_id>/deactivate", methods=["PATCH"])
def deactivate_merchant(merchant_id):
    merchant = Merchant.query.get(merchant_id)

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    merchant.is_active = False
    db.session.commit()

    return jsonify({
        "message": "Merchant deactivated successfully"
    }), 200


@merchants_bp.route("/<int:merchant_id>/activate", methods=["PATCH"])
def activate_merchant(merchant_id):
    merchant = Merchant.query.get(merchant_id)

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    merchant.is_active = True
    db.session.commit()

    return jsonify({
        "message": "Merchant activated successfully"
    }), 200


@merchants_bp.route("/<int:merchant_id>", methods=["DELETE"])
def delete_merchant(merchant_id):
    merchant = Merchant.query.get(merchant_id)

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    db.session.delete(merchant)
    db.session.commit()

    return jsonify({
        "message": "Merchant deleted successfully"
    }), 200