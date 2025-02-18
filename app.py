from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola! Esta es mi aplicación web desplegada en OpenShift."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

