from flask import Blueprint, jsonify, request
from app.models import Product
from app import db

bp = Blueprint("product", __name__, url_prefix="/products")

@bp.route("/", methods=["GET"])
def list_products():
    products = Product.query.all()
    result = [
        {"id": p.id, "name": p.name, "description": p.description, "price": p.price, "stock": p.stock}
        for p in products
    ]
    return jsonify(result), 200

@bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data["name"],
        description=data.get("description", ""),
        price=data["price"],
        stock=data["stock"]
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created!"}), 201