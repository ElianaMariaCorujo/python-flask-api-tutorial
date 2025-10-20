from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

# --- ESTA ES LA VERSIÓN CORRECTA ---
# Sigue las instrucciones: Recibe <int:position>
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position): # <- 1. Recibe la posición
    
    # Validamos que la 'position' (índice) exista
    if position >= len(todos) or position < 0:
        return jsonify({"error": "Posición inválida"}), 400
    
    # 2. Elimina la tarea usando la posición (índice)
    todos.pop(position)
    
    # 3. Retorna la lista actualizada
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)