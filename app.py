from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Aquí guardaremos los datos temporalmente
datos_sensor = []

@app.route('/sensordata', methods=['POST'])
def recibir_datos():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    data["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datos_sensor.append(data)
    print("Dato recibido:", data)
    return jsonify({"mensaje": "Dato recibido correctamente"}), 200

@app.route('/')
def dashboard():
    return render_template('dashboard.html', datos=datos_sensor[-10:])  # Muestra solo los últimos 10

if __name__ == '__main__':
    app.run(debug=True)
