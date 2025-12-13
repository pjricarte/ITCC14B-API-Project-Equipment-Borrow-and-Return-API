from flask import Blueprint, request, jsonify
from .models import Item, User, Transaction, db

items_bp = Blueprint("items", __name__)
users_bp = Blueprint("users", __name__) 
borrow_bp = Blueprint("borrow", __name__)


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
    
@borrow_bp.route("/borrow", methods=["POST"])
def borrow_item():
    data = request.get_json()
    user_id = data.get("user_id")
    item_id = data.get("item_id")
    
    if not user_id or not item_id:
        return jsonify({"message": "Both 'user_id' and 'item_id' are required."}), 400
    
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404
    
    if item.amount < 1:
        return jsonify({"message": "Item not available"}), 400
    
    error = update_item_amount(item, item.amount - 1)
    if error:
        return jsonify(error[0]), error[1]
    
    transaction = Transaction(
        user_id=user_id,
        item_id=item_id,
        action="borrow",
        quantity=1  
    )
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify({"message": "Item borrowed successfully!", "item": item.to_dict()}), 200


@borrow_bp.route("/returns", methods=["POST"])
def return_item():
    data = request.get_json()
    user_id = data.get("user_id")
    item_id = data.get("item_id")
    
    if not user_id or not item_id:
        return jsonify({"message": "Both 'user_id' and 'item_id' are required."}), 400
    
    borrow_count = Transaction.query.filter_by(
        user_id=user_id,
        item_id=item_id,
        action="borrow"
    ).count()
    
    return_count = Transaction.query.filter_by(
        user_id=user_id,
        item_id=item_id,
        action="return"
    ).count()
    
    if borrow_count <= return_count:
        return jsonify({"message": "No borrowed item to return."}), 400

    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404

    error = update_item_amount(item, item.amount + 1)
    if error:
        return jsonify(error[0]), error[1]
    
    transaction = Transaction(
        user_id=user_id,
        item_id=item_id,
        action="return",
        quantity=1
    )
    
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Item returned successfully!", "item": item.to_dict()}), 200

@borrow_bp.route("/transactions", methods=["GET"])
def list_transactions():
    transactions = Transaction.query.all()
    if not transactions:
        return jsonify({"message": "No transactions found."}), 404
    
    return jsonify([t.to_dict() for t in transactions]), 200
    
@borrow_bp.route("/transactions/users/<int:user_id>", methods=["GET"])
def get_user_transactions(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    if not transactions:
        return jsonify({"message": "No transactions found for this user."}), 404

    return jsonify([t.to_dict() for t in transactions]), 200

@borrow_bp.route("/transactions/items/<int:item_id>", methods=["GET"])
def get_item_transactions(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404

    transactions = Transaction.query.filter_by(item_id=item_id).all()
    if not transactions:
        return jsonify({"message": "No transactions found for this item."}), 404

    result = []
    for t in transactions:
        record = {
            "id": t.id,
            "action": t.action,
            "quantity": t.quantity,
            "timestamp": t.timestamp.isoformat() if t.timestamp else None,
            "user": {
                "id": t.user.id,
                "username": t.user.username,
                "first_name": t.user.first_name,
                "last_name": t.user.last_name
            } if t.user else None,
            "item": {
                "id": t.item.id,
                "name": t.item.name,
                "category": t.item.category
            } if t.item else None
        }
        result.append(record)

    return jsonify(result), 200

def update_item_amount(item, new_amount):
    if new_amount < 0:
        return {"error": "'amount' must be non-negative"}, 400

    item.amount = new_amount
    db.session.commit()
    return None
