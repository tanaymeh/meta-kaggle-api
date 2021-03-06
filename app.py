import json
from flask import Flask, jsonify, request 

app = Flask(__name__)

@app.route('/rank', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        with open("ranks.json", "w") as f:
            json.dump(data, f)
        return "Request Sent Successfully!"
    else:
        with open("ranks.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    return "Work done!"

app.run()