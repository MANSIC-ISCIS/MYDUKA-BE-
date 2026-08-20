from flask import Blueprint, request, jsonify
from extensions import db
from models.clerk import Clerk

clerk = Blueprint("clerk", __name__)

# A clerk route to create a new clerk
@clerk.route("/clerks", methods=["POST"])
def create_clerk():
    data = request.get_json()

    clerk_name = data.get("clerk_name")
    admin_id = data.get("admin_id")
    store_id = data.get("store_id")

    if not clerk_name or not admin_id or not store_id:
        return jsonify({"error": "clerk_name, admin_id and store_id are required."}), 400

    new_clerk = Clerk(clerk_name=clerk_name, admin_id=admin_id,
        store_id=store_id )

    db.session.add(new_clerk)
    db.session.commit()

    return jsonify({"message": "Clerk created successfully.",
        "clerk_id": new_clerk.clerk_id }), 201