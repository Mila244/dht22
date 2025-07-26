from flask import Flask, request, jsonify
import os

app = Flask(__name__)

datos_sensor = []  # Para guardar los datos recibidos

@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "Backend Flask funcionando 🚀", "datos": datos_sensor})

@app.route('/sensor', methods=['POST'])
def recibir_datos():
    data = request.get_json()
    datos_sensor.append(data)
    print(f"📥 Datos recibidos: {data}")
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
