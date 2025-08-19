from flask import Flask, request, jsonify

# Объект Flask должен называться "app" для gunicorn
app = Flask(__name__)

# Простейший маршрут для проверки
@app.route("/", methods=["GET"])
def home():
    return "Server is running!"

# Пример маршрута для получения данных из .exe
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json  # ожидаем JSON
    print("Received data:", data)
    return jsonify({"status": "success"}), 200

# Проверка запуска локально
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
