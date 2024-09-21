from flask import Flask, request, jsonify, make_response
from flask_cors import CORS  # Import CORS to handle cross-origin requests
from pymongo import MongoClient
import datetime
from bson import json_util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Connect to local MongoDB
db = client['github_webhooks']  # Use 'github_webhooks' database
collection = db['actions']  # Collection to store GitHub actions

# Webhook endpoint to receive GitHub events
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get the JSON payload from GitHub
    print(data)  # Log the payload for debugging

    if not data:
        return jsonify({'message': 'No data received'}), 400

    # Process and store the GitHub action in MongoDB
    if 'action' in data:
        action_data = {
            'author': data['sender']['login'],
            'action_type': data['action'],
            'repo': data['repository']['name'],
            'to_branch': data['ref'].split('/')[-1] if 'ref' in data else None,
            'timestamp': datetime.datetime.utcnow()
        }
        collection.insert_one(action_data)  # Insert action data into MongoDB
        return jsonify({'message': 'Success'}), 200

    return jsonify({'message': 'No action found'}), 400

# Endpoint to fetch the latest GitHub actions from MongoDB
@app.route('/get-latest-actions', methods=['GET'])
def get_latest_actions():
    actions = list(collection.find().sort('timestamp', -1).limit(10))  # Fetch latest 10 actions
    response = make_response(json_util.dumps(actions), 200)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == '__main__':
    app.run(port=5000)  # Run the app on port 5000
