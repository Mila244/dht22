from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sensordata', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    temperatura = datos.get('temperatura')
    humedad = datos.get('humedad')
    
    print(f"Temperatura: {temperatura}°C | Humedad: {humedad}%")
    
    return jsonify({"status": "Datos recibidos"}), 200

# Para Render, no pongas host='localhost'
if __name__ == '__main__':
    app.run()
