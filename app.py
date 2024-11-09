from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
message = ""

@app.route("/lcd")
def home():
    return render_template("index.html")

@app.route("/lcd/api/get_message", methods=["GET"])
def get_message():
    return {"message": message}

@app.route("/lcd/api/set_message", methods=["POST"])
def set_message():
    data = request.get_json()
    if data:
        message = data.get("message")
        return jsonify({"status": "success", "message": message}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
