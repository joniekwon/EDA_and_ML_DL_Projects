from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/server-health-check", methods=["GET"])
def server_health_check():
    return jsonify({"result": "ok"}), 200

@app.route("/echo", methods=["POST"])
def echo():
    try:
        data = request.get_json()
        name = data.get("name")
        message = data.get("message")
        if not isinstance(name, str) or not isinstance(message, str):
            raise Exception
        return jsonify({"name":name, "message":message})
    except Exception:
        return jsonify({"error":"Invalid data format"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678, debug=True)
