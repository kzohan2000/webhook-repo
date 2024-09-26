GitHub Event Webhook Tracker
This project is designed to automate the tracking of events such as Push, Pull Request, and Merge in a GitHub repository by triggering webhooks. The system logs these events in MongoDB for real-time tracking and analysis, helping to streamline development workflows.

Features
Automated Webhooks: Automatically triggers for GitHub events like Push, Pull Request, and Merge.
Event Logging: Logs event data in MongoDB for future analysis.
Real-Time Tracking: Provides real-time updates for important GitHub repository actions.
Extensible: Easily extend the project to handle additional events or integrate with other tools.
Technologies Used
Node.js - Backend server to handle webhook events.
Express - Web framework for setting up the webhook endpoint.
MongoDB - Database to store and analyze the incoming events.
GitHub API - To fetch and manage repository events.
Prerequisites
Node.js installed on your machine
MongoDB installed and running locally or on the cloud (e.g., MongoDB Atlas)
A GitHub account with a repository to set up webhooks
Setup Guide
Clone the Repository

bash
Copy code
git clone https://github.com/kzohan2000/webhook-repo.git
cd webhook-repo
Install Dependencies

bash
Copy code
npm install
Set Up MongoDB

Ensure MongoDB is running, and update the config.js file with your MongoDB connection details.

Configure Webhook Endpoint

Go to your GitHub repository.
Navigate to Settings > Webhooks > Add Webhook.
Set the Payload URL to the server endpoint where the webhook receiver is hosted.
Set Content type to application/json.
Choose events like push, pull request, merge, or select Send me everything.
Run the Server

bash
Copy code
npm start
The server will now listen for GitHub events and store the event data in MongoDB.

Event Logging
The incoming GitHub events are logged in MongoDB. Each event is stored with the following structure:

json
Copy code
{
  "event_type": "push",
  "repository": "your-repo-name",
  "timestamp": "2024-09-27T10:20:30Z",
  "payload": {
    // GitHub event details
  }
}
Extending the Project
To handle additional GitHub events, simply modify the eventHandler.js file and add support for more event types, as needed.

Future Enhancements
Dashboard for visualizing event data.
Integration with other CI/CD tools.
Alerting system for critical repository actions.
