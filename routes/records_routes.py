from flask import Blueprint, request, jsonify
from extensions import db
from models.records import Record

records_bp = Blueprint("records_bp", __name__)

# Route to create a record
@records_bp.route("/records", methods=["POST"])
def create_record():
    data = request.get_json()

    required_fields = ["clerk_id", "product_id",
        "items_received", "items_in_stock",
        "buying_price","selling_price",
        "store_id","admin_id"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_record = Record(clerk_id=data["clerk_id"],
        product_id=data["product_id"],
        items_received=data["items_received"], items_in_stock=data["items_in_stock"],
        items_spoilt=data.get("items_spoilt", 0),
        buying_price=data["buying_price"], selling_price=data["selling_price"],
        store_id=data["store_id"], admin_id=data["admin_id"], supplier_id=data.get("supplier_id", None))

    db.session.add(new_record)
    db.session.commit()

    return jsonify({"message": "Record created successfully",
        "record_id": new_record.record_id}), 201

# Route to get all records
@records_bp.route("/records", methods=["GET"])
def get_records():
    records = Record.query.all()

    return jsonify([
        {"record_id": record.record_id, "clerk_id": record.clerk_id,
            "product_id": record.product_id, "items_received": record.items_received,
            "items_in_stock": record.items_in_stock,"items_spoilt": record.items_spoilt,
            "buying_price": float(record.buying_price),
            "selling_price": float(record.selling_price),
            "payment_status": record.payment_status,"store_id": record.store_id,
            "admin_id": record.admin_id,"created_at": record.created_at
        }
        for record in records]), 200