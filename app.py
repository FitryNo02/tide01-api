from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "tide_height": "5.35m",
        "tide_time": "6:20AM"
    })

app.run(host="0.0.0.0", port=10000)
