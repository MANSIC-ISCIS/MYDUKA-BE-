from flask import Blueprint, request, jsonify
from extensions import db
from models.records import Record
from models.payments import Payment

payment = Blueprint("payment", __name__)

#  Route to create a payment
@payment.route("/payments", methods=["POST"])
def create_payment():
    data = request.get_json()

    record_id = data.get("record_id")
    amount = data.get("amount")
    phone_number = data.get("phone_number")

    if not record_id or not amount or not phone_number:
        return jsonify({"error": "record_id, amount and phone_number are required"}), 400
    record = Record.query.get(record_id)

    if not record:
        return jsonify({"error": "Record not found"}), 404

    new_payment = Payment(record_id=record_id,
        amount=amount,
        phone_number=phone_number)

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({"message": "Payment created successfully",
        "payment_id": new_payment.payment_id,
        "status": new_payment.status}), 201

# Route to get all payments
@payment.route("/payments", methods=["GET"])
def get_payments():
    payments = Payment.query.all()

    return jsonify([
        {"payment_id": p.payment_id, "record_id": p.record_id,
            "amount": float(p.amount),"phone_number": p.phone_number,
            "status": p.status,"created_at": p.created_at
        }
        for p in payments
    ]), 200

# Route to get one payment
@payment.route("/payments/<int:payment_id>", methods=["GET"])
def get_payment(payment_id):
    payment_record = Payment.query.get(payment_id)

    if not payment_record:
        return jsonify({"error": "Payment not found"}), 404

    return jsonify({"payment_id": payment_record.payment_id,
        "record_id": payment_record.record_id,
        "amount": float(payment_record.amount),
        "phone_number": payment_record.phone_number,
        "status": payment_record.status,
        "mpesa_receipt_number": payment_record.mpesa_receipt_number
    }), 200