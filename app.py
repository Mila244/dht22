from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask corriendo en Render 🎉"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto por variable de entorno
    app.run(host='0.0.0.0', port=port)