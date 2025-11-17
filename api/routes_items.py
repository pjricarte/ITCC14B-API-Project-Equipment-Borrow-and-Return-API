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
        description=data.get("description", "")
    )

    db.session.add(new_item)
    db.session.commit()

    return jsonify({
        "message": "Item added successfully!",
        "item_id": new_item.id
    }), 201