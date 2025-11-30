from flask import Blueprint, request, jsonify
from .models import Item, User, db

items_bp = Blueprint("items", __name__)
users_bp = Blueprint("users", __name__) 


@items_bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    if not items:
        return jsonify({"message": "No items found."}), 404
    return jsonify([i.to_dict() for i in items]), 200


@items_bp.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid request. JSON data is required."}), 400

    required_fields = ["name", "category", "amount", "description"]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return jsonify({"message": f"'{field}' is required."}), 400

    name = data["name"].strip()
    category = data["category"].strip()
    description = data["description"].strip()   

    try:
        amount = int(data["amount"])
    except ValueError:
        return jsonify({"message": "'amount' must be a number"}), 400

    if amount < 1:
        return jsonify({"message": "'amount' must be a positive integer"}), 400

    existing_item = Item.query.filter_by(name=name, category=category).first()
    if existing_item:
        return jsonify({"message": "Item already exists."}), 400

    new_item = Item(
        name=name,
        category=category,
        amount=amount,
        description=description
    )
    
    db.session.add(new_item)
    db.session.commit()

    return jsonify({"message": "Item added successfully.", "item": new_item.to_dict()}), 201



@items_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item_by_id(item_id):
    item = Item.query.get(item_id)
    if item:
        return jsonify(item.to_dict()), 200
    else:
        return jsonify({"message": "Item not found"}), 404


@items_bp.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid request. JSON data is required."}), 400

    amount = data.get("amount")
    if amount is not None:
        if not isinstance(amount, int) or amount < 0:
            return jsonify({"message": "'amount' must be a non-negative integer"}), 400
        item.amount = amount

    item.name = data.get("name", item.name)
    item.category = data.get("category", item.category)
    item.status = data.get("status", item.status)
    item.description = data.get("description", item.description)

    db.session.commit()

    return jsonify({"message": "Item updated successfully!"}), 200

@items_bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_items(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404
    
    db.session.delete(item)
    db.session.commit()
    
    return jsonify({"message": "Item deleted successfully!"}), 200

@items_bp.route("/items/search", methods=["GET"])
def search_items():
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"message": "Search term is required."}), 400
    
    results = Item.query.filter(
        db.or_(
            Item.name.ilike(f"%{query}%") |
            Item.category.ilike(f"%{query}%") |
            Item.description.ilike(f"%{query}%") |
            Item.status.ilike(f"%{query}%")
        )  
    ) .all()
    
    if not results:
        return jsonify({"message": "No items found matching the search criteria."}), 404

    return jsonify([item.to_dict() for item in results]), 200

@users_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    required_fields = ["username", "first_name", "last_name", "email", "password"]
    for field in required_fields:
        if field not in data or not data[field].strip():
            return jsonify({"message": f"'{field}' is required."}), 400
        
    username = data["username"].strip()
    first_name = data["first_name"].strip()
    last_name = data["last_name"].strip()
    email = data["email"].strip()
    password = data["password"].strip()
    
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()
    if existing_user:
        return jsonify({"message": "Username or email already exists."}), 400
    
    from werkzeug.security import generate_password_hash
    hashed_password = generate_password_hash(password)
    
    new_user = User(
        username=username, 
        first_name=first_name, 
        last_name=last_name, email=email, 
        password=hashed_password
    )
    
    db.session.add(new_user)    
    db.session.commit()
    
    return jsonify({"message": "User added successfully.", "user": new_user.to_dict()}), 201

@users_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    if not users:
        return jsonify({"message": "No users found."}), 404
    return jsonify([user.to_dict() for user in users]), 200       