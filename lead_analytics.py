from flask import Flask, request, jsonify

app = Flask(__name__)

leads = []

@app.route("/store_lead", methods=["POST"])
def store_lead():
    data = request.get_json()
    if data:
        leads.append(data)
        return jsonify({"message": "Lead stored successfully!", "total_leads": len(leads)}), 201
    return jsonify({"error": "Invalid data"}), 400

@app.route("/get_leads", methods=["GET"])
def get_leads():
    return jsonify({"leads": leads}), 200

if __name__ == "__main__":
    app.run(port=5001, debug=True)  # Run Lead Analytics on a different port