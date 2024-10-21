from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON payload from the request
    data = request.json

    # Print the entire payload for debugging
    print(f"Received webhook data: {data}")

    # Extract relevant information about the commit
    if 'head_commit' in data:
        commit_message = data['head_commit']['message']
        author_name = data['head_commit']['author']['name']
        commit_url = data['head_commit']['url']
        timestamp = data['head_commit']['timestamp']

        # Print specific commit information
        print(f"New commit received!")
        print(f"Commit message: {commit_message}")
        print(f"Author: {author_name}")
        print(f"Commit URL: {commit_url}")
        print(f"Timestamp: {timestamp}")

    return jsonify({'status': 'success'}), 200

@app.route('/favicon.ico')  # Optional: to handle favicon requests
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(port=5000)
