from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Handle the push event
    if 'pusher' in data:
        print(f"New commit pushed by {data['pusher']['name']}: {data['head_commit']['message']}")
        # Process the commit data as needed
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)
