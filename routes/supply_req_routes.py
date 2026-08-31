from flask import Blueprint, request, jsonify
from extensions import db
from models.supply_rep import SupplyRequest

supply_req_bp = Blueprint('supply_requests', __name__)

@supply_req_bp.route('/supply-requests', methods=['GET'])
def get_supply_requests():
    requests = SupplyRequest.query.all()
    return jsonify([{
        'id': r.id,
        'product_name': r.product_name,
        'product_id': r.product_id,
        'store_name': r.store_name,
        'store_id': r.store_id,
        'clerk_name': r.clerk_name,
        'clerk_id': r.clerk_id,
        'quantity_requested': r.quantity_requested,
        'reason': r.reason,
        'status': r.status,
        'created_at': r.created_at.strftime('%Y-%m-%d %H:%M:%S') if r.created_at else None
    } for r in requests]), 200

@supply_req_bp.route('/supply-requests', methods=['POST'])
def create_supply_request():
    data = request.get_json()
    new_request = SupplyRequest(
        product_name=data['product_name'],
        product_id=data['product_id'],
        store_name=data.get('store_name'),
        store_id=data.get('store_id'),
        clerk_name=data.get('clerk_name'),
        clerk_id=data.get('clerk_id'),
        quantity_requested=data['quantity_requested'],
        reason=data.get('reason'),
        status='Pending'
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'Supply request created successfully'}), 201