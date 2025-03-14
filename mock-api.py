from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

# PostgreSQL Config
DATABASE_URL = "postgresql://postgres@localhost:5432/evvy_db"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define Models
class CartEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Ensure database tables are created
with app.app_context():
    db.create_all()

# API Endpoint
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    data = request.json
    event = CartEvent(user_id=data["user_id"], product_id=data["product_id"])
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Added to cart", "event": {"user_id": event.user_id, "product_id": event.product_id, "timestamp": event.timestamp}}), 201

if __name__ == "__main__":
    app.run(debug=True)

# Simulated database (in-memory)
cart_events = []
purchases = []
subscriptions = []
product_views = []

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    data = request.json
    event = CartEvent(user_id=data["user_id"], product_id=data["product_id"])
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Added to cart", "event": {"user_id": event.user_id, "product_id": event.product_id, "timestamp": event.timestamp}}), 201

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.json
    event = {
        "user_id": data["user_id"],
        "product_id": data["product_id"],
        "price": data["price"],
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    purchases.append(event)
    return jsonify({"message": "Purchase completed", "event": event}), 201

@app.route("/subscription_change", methods=["POST"])
def subscription_change():
    data = request.json
    event = {
        "user_id": data["user_id"],
        "subscription_status": data["status"],
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    subscriptions.append(event)
    return jsonify({"message": "Subscription updated", "event": event}), 201

@app.route("/product_views", methods=["POST"])
def product_views_log():
    data = request.json
    event = {
        "user_id": data["user_id"],
        "product_id": data["product_id"],
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    product_views.append(event)
    return jsonify({"message": "Product viewed", "event": event}), 201

if __name__ == "__main__":
    app.run(debug=True)
