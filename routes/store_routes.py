from flask import Blueprint, request, jsonify
from extensions import db
from models.store import Store
from models.merchants import Merchant
from schemas.store_schema import (
    store_schema,
    stores_schema
)


store_bp = Blueprint(
    "stores",
    __name__,
    url_prefix="/stores"
)


@store_bp.route("/stores", methods=["POST"])
def create_store():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    st_name = data.get("name") or data.get("st_name")
    location = data.get("location")
    merchant_id = data.get("merchantid") or data.get("merchant_id")

    if not st_name:
        return jsonify({
            "error": "st_name are required"
        }), 400

    if not location: 
        return jsonify({
            "error": "location are required"
        }), 400

    if not merchant_id:
        return jsonify({
            "error": "merchant_id are required"
        }), 400

    merchant = db.session.get(
        Merchant,
        merchant_id
    )


    store = Store(
        st_name=st_name,
        location=location,
        merchant_id=merchant_id
    )

    db.session.add(store)
    db.session.commit()

    return jsonify({
        "message": "Store created successfully",
        "store": store_schema.dump(store)
    }), 201


@store_bp.route("/stores", methods=["GET"])
def get_stores():
    stores = Store.query.all()

    return jsonify({
        "stores": stores_schema.dump(stores)
    }), 200


@store_bp.route("/stores/<int:store_id>", methods=["GET"])
def get_store(store_id):
    store = db.session.get(Store, store_id)

    if not store:
        return jsonify({
            "error": "Store not found"
        }), 404

    return jsonify({
        "store": store_schema.dump(store)
    }), 200


@store_bp.route(
    "/merchant/<int:merchant_id>",
    methods=["GET"]
)
def get_merchant_stores(merchant_id):
    merchant = db.session.get(
        Merchant,
        merchant_id
    )

    if not merchant:
        return jsonify({
            "error": "Merchant not found"
        }), 404

    stores = Store.query.filter_by(
        merchant_id=merchant_id
    ).all()

    return jsonify({
        "stores": stores_schema.dump(stores)
    }), 200


@store_bp.route(
    "/stores/<int:store_id>",
    methods=["PUT"]
)
def update_store(store_id):
    store = db.session.get(Store, store_id)

    if not store:
        return jsonify({
            "error": "Store not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "st_name" in data:
        store.st_name = data["st_name"]

    if "location" in data:
        store.location = data["location"]

    if "merchant_id" in data:
        merchant = db.session.get(
            Merchant,
            data["merchant_id"]
        )

        if not merchant:
            return jsonify({
                "error": "Merchant not found"
            }), 404

        store.merchant_id = data["merchant_id"]

    db.session.commit()

    return jsonify({
        "message": "Store updated successfully",
        "store": store_schema.dump(store)
    }), 200


@store_bp.route(
    "/stores/<int:store_id>",
    methods=["DELETE"]
)
def delete_store(store_id):
    store = db.session.get(Store, store_id)

    if not store:
        return jsonify({
            "error": "Store not found"
        }), 404

    db.session.delete(store)
    db.session.commit()

    return jsonify({
        "message": "Store deleted successfully"
    }), 200