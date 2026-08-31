import secrets
from datetime import datetime, timedelta

from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity

from extensions import db
from models.user import user
from models.invitation import Invitation
from utils.permission import role_required


merchant_bp = Blueprint(
    "merchant",
    __name__,
    url_prefix="/merchant"
)


@merchant_bp.route("/invite-admin", methods=["POST"])
@role_required(user.MERCHANT)
def invite_admin():

    data = request.get_json()

    email = data.get("email")

    if not email:
        return jsonify({
            "error": "Admin email is required"
        }), 400

    # Check if email is already registered
    existing_user = user.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return jsonify({
            "error": "This email is already registered"
        }), 409

    # Generate secure invitation token
    token = secrets.token_urlsafe(32)

    # Token expires after 24 hours
    expires_at = datetime.utcnow() + timedelta(hours=24)

    # Get merchant ID from JWT
    merchant_id = get_jwt_identity()

    invitation = Invitation(
        email=email,
        role=user.ADMIN,
        token=token,
        expires_at=expires_at,
        invited_by=int(merchant_id)
    )

    db.session.add(invitation)
    db.session.commit()

    # For testing only
    invitation_link = (
        f"http://localhost:5173/register/admin/{token}"
    )

    return jsonify({
        "message": "Admin invitation created",
        "invitation_link": invitation_link
    }), 201