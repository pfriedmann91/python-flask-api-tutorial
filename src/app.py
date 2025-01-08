from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    if len(todos) == 0:
        return jsonify({"message": "No tasks available"}), 200
    else:
        return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    if not request_body:
        return jsonify({"error": "Request body is missing"}), 400
    else:
        todos.append(request_body)
        return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Position does not exist"}), 404
    else:
        deleted_task = todos.pop(position)
        return jsonify(todos), 200

# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
