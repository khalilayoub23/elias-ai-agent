
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    data = request.json
    response = {"message": "Elias API received your data!", "data": data}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
