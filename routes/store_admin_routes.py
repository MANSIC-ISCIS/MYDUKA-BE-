from flask import Blueprint, request, jsonify
from extensions import db
from models.store_admin import StoreAdmin
from models.merchants import Merchant
from models.store import Store
from schemas.store_admin_schema import (
    store_admin_schema,
    store_admins_schema
)

store_admin_bp = Blueprint(
    "store_admins",
    __name__,
    url_prefix="/api/store-admins"
)


@store_admin_bp.route("/", methods=["POST"])
def create_store_admin():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    admin_name = data.get("admin_name")
    merchant_id = data.get("merchant_id")
    store_id = data.get("store_id")

    if not admin_name or not merchant_id or not store_id:
        return jsonify({
            "error": "admin_name, merchant_id and store_id are required"
        }), 400

    merchant = db.session.get(Merchant, merchant_id)

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    store = db.session.get(Store, store_id)

    if not store:
        return jsonify({
            "error": "Store not found"
        }), 404

    if store.merchant_id != merchant_id:
        return jsonify({
            "error": "Store does not belong to this merchant"
        }), 400

    admin = StoreAdmin(
        admin_name=admin_name,
        merchant_id=merchant_id,
        store_id=store_id
    )

    db.session.add(admin)
    db.session.commit()

    return jsonify({
        "message": "Store admin created successfully",
        "admin": store_admin_schema.dump(admin)
    }), 201


@store_admin_bp.route("/", methods=["GET"])
def get_store_admins():
    admins = StoreAdmin.query.all()

    return jsonify({
        "admins": store_admins_schema.dump(admins)
    }), 200


@store_admin_bp.route("/<int:admin_id>", methods=["GET"])
def get_store_admin(admin_id):
    admin = db.session.get(StoreAdmin, admin_id)

    if not admin:
        return jsonify({
            "error": "Store admin not found"
        }), 404

    return jsonify({
        "admin": store_admin_schema.dump(admin)
    }), 200


@store_admin_bp.route("/merchant/<int:merchant_id>", methods=["GET"])
def get_merchant_admins(merchant_id):
    merchant = db.session.get(Merchant, merchant_id)

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    admins = StoreAdmin.query.filter_by(
        merchant_id=merchant_id
    ).all()

    return jsonify({
        "admins": store_admins_schema.dump(admins)
    }), 200


@store_admin_bp.route("/store/<int:store_id>", methods=["GET"])
def get_store_admins_by_store(store_id):
    store = db.session.get(Store, store_id)

    if not store:
        return jsonify({
            "error": "Store not found"
        }), 404

    admins = StoreAdmin.query.filter_by(
        store_id=store_id
    ).all()

    return jsonify({
        "admins": store_admins_schema.dump(admins)
    }), 200


@store_admin_bp.route("/<int:admin_id>", methods=["PUT"])
def update_store_admin(admin_id):
    admin = db.session.get(StoreAdmin, admin_id)

    if not admin:
        return jsonify({
            "error": "Store admin not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "admin_name" in data:
        admin.admin_name = data["admin_name"]

    if "merchant_id" in data:
        merchant = db.session.get(
            Merchant,
            data["merchant_id"]
        )

        if not merchant:
            return jsonify({
                "error": "Merchant not found"
            }), 404

        admin.merchant_id = data["merchant_id"]

    if "store_id" in data:
        store = db.session.get(
            Store,
            data["store_id"]
        )

        if not store:
            return jsonify({
                "error": "Store not found"
            }), 404

        if store.merchant_id != admin.merchant_id:
            return jsonify({
                "error": "Store does not belong to this merchant"
            }), 400

        admin.store_id = data["store_id"]

    db.session.commit()

    return jsonify({
        "message": "Store admin updated successfully",
        "admin": store_admin_schema.dump(admin)
    }), 200


@store_admin_bp.route(
    "/<int:admin_id>/deactivate",
    methods=["PATCH"]
)
def deactivate_store_admin(admin_id):
    admin = db.session.get(StoreAdmin, admin_id)

    if not admin:
        return jsonify({
            "error": "Store admin not found"
        }), 404

    db.session.delete(admin)
    db.session.commit()

    return jsonify({
        "message": "Store admin deactivated successfully"
    }), 200


@store_admin_bp.route("/<int:admin_id>", methods=["DELETE"])
def delete_store_admin(admin_id):
    admin = db.session.get(StoreAdmin, admin_id)

    if not admin:
        return jsonify({
            "error": "Store admin not found"
        }), 404

    db.session.delete(admin)
    db.session.commit()

    return jsonify({
        "message": "Store admin deleted successfully"
    }), 200
