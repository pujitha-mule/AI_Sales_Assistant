from flask import Flask, request, jsonify
from app.agent import SalesAgent

app = Flask(__name__)
agent = SalesAgent()

@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get('query')
    return jsonify({'response': agent.handle_query(query)})

if __name__ == '__main__':
    app.run(debug=True)
