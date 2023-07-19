from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/members")
def members():
    data = {"msg": "Hello"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
