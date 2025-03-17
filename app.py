"""
Author: Angel Ruiz Zafra
License: MIT License
Version: 2025.2.1
Repository: https://github.com/pid-chatbots-ugr/pid-backend
Created on 17/3/25 by Angel Ruiz Zafra
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, mundo! Esta es una API Flask en el puerto 5000."

@app.route('/hello')
def hello():
    return "¡Hola desde Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
