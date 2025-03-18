"""
Author: Angel Ruiz Zafra
License: MIT License
Version: 2025.2.1
Repository: https://github.com/pid-chatbots-ugr/pid-backend
Created on 17/3/25 by Angel Ruiz Zafra
"""
import time

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin  # Importar Flask-CORS

from ai.ai import OpenAI
from db.mongodb_manager import MongoDBManager

openai = OpenAI()
openai.initClient()

mdb = MongoDBManager()

app = Flask(__name__)
CORS(app)  # Habilitar CORS en la aplicación
@app.route('/')
def index():
    data = request.json  # Equivalente a request.get_json()

    return jsonify({"message": "Datos recibidos", "data": data})

@app.route('/chat', methods=['POST'])
#@cross_origin(origins=["http://localhost:3000"]) #solo este dominio
def chat():
    timestamp = time.time()
    data  = request.json
    print("DATA : ",data)
    message = data.get("message")
    # Preguntar a OpenAI
    response = openai.request(message)
    # Guardar la conversación en MongoDB
    conversacion = {"message": message, "response": response}
    mdb.insertar_conversacion(data.get("user"), conversacion, data.get("metadata"), timestamp)
    return {"response":response}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
