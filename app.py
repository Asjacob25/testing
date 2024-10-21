from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub token

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON payload from the request
    data = request.json

    # Print the entire payload for debugging
    print(f"Received webhook data: {data}")

    # Extract relevant information about the commit
    if 'head_commit' in data:
        commit_sha = data['head_commit']['id']
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

        # Fetch the actual code changes from the GitHub API
        fetch_code_changes(commit_sha)

    return jsonify({'status': 'success'}), 200

def fetch_code_changes(commit_sha):
    # Make a request to the GitHub API to get commit details
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',  # Authenticate using your GitHub token
        'Accept': 'application/vnd.github.v3+json',
    }
    
    # Change 'username' and 'repo' to your GitHub username and repository name
    response = requests.get(f"{GITHUB_API_URL}/repos/username/repo/commits/{commit_sha}", headers=headers)

    if response.status_code == 200:
        commit_data = response.json()
        # Extract the files changed in the commit
        files_changed = commit_data.get('files', [])
        print("Files changed in this commit:")
        for file in files_changed:
            print(f"Filename: {file['filename']}")
            print(f"Status: {file['status']}")
            print(f"Changes: {file['changes']} lines changed")
            print("-" * 30)
    else:
        print(f"Failed to fetch code changes: {response.status_code} {response.text}")

@app.route('/favicon.ico')  # Optional: to handle favicon requests
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(port=5000)
