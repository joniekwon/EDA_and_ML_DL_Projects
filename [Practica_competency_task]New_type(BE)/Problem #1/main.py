from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

DATA_DIR = "./data/input"

with open(f"{DATA_DIR}/reservation.json", "r") as file:
     reservation = json.load(file)


@app.route("/api/reservation/search", methods=["GET"])
def search_reservation():
    try:
        customer_name = request.args.get('customerName')
        if customer_name is None:
            return jsonify({"error": "customerName is required"}), 400

        search_results = []

        if customer_name == 'all':
            search_results = reservation[:]
        else:
            for i, resv in enumerate(reservation):
                # if resv["customer_name"].startswith(customer_name):
                if customer_name in resv["customer_name"]:
                    search_results.append(reservation[i])
        if search_results:
            search_results = sorted(search_results, key=lambda x: x["check_in"])

        return jsonify(search_results), 200

    except Exception as e:
        return "Internal Server Error", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678, debug=True)
