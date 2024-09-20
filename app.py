from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['github_webhooks']
collection = db['actions']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Extract the JSON payload from GitHub

    # Check if the data contains a valid action
    if 'action' in data:
        action_data = {
            'author': data['sender']['login'],
            'action_type': data['action'],
            'repo': data['repository']['name'],
            'to_branch': data['ref'].split('/')[-1] if 'ref' in data else None,
            'timestamp': datetime.datetime.utcnow()
        }
        collection.insert_one(action_data)
        return jsonify({'message': 'Success'}), 200
    return jsonify({'message': 'No action found'}), 400

if __name__ == '__main__':
    app.run(port=5000)
