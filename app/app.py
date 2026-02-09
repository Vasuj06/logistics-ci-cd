from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Logistics Service",
        "status": "Running",
        "version": "1.0"
    })

# Health check endpoint (VERY IMPORTANT for DevOps)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200

# Sample logistics API (create order)
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
        host="0.0.0.0",   # 🔴 REQUIRED FOR DOCKER
        port=5000,        # 🔴 MUST MATCH Dockerfile
        debug=False
    )
