from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Flask funcionando correctamente en Render 🎉"

if __name__ == '__main__':
    # Render asigna el puerto automáticamente a través de la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
