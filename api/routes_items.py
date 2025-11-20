from flask import Blueprint, request, jsonify
from .models import Item, db

items_bp = Blueprint("items", __name__)

@items_bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([i.to_dict() for i in items]), 200


@items_bp.route("/items/add", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = Item(
        name=data["name"],
        category=data["category"],
        amount=data.get("amount", 1),
        description=data.get("description", "")
    )

    db.session.add(new_item)
    db.session.commit()

    return jsonify({
        "message": "Item added successfully!",
        "item_id": new_item.id
    }), 201
    
@items_bp.route("/items/<int:item_id>", methods=["GET"])
def get_itemsID(item_id):
    item = Item.query.get(item_id)
    if item:
        return jsonify(item.to_dict()), 200
    else:
        return jsonify({"message": "Item not found"}), 404
