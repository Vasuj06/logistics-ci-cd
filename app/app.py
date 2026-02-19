from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Logistics Service",
        "status": "Running",
        "version": "1.0"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json()

    if not data or "order_id" not in data:
        return jsonify({"error": "Invalid order data"}), 400

    return jsonify({
        "message": "Order created successfully",
        "order_id": data["order_id"]
    }), 201

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
