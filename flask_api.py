from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/api/endpoint1', methods=['GET'])
def endpoint1():
    time.sleep(2)  # 擬似的な遅延
    return jsonify({"message": "Response from endpoint1"})

@app.route('/api/endpoint2', methods=['GET'])
def endpoint2():
    time.sleep(2)
    return jsonify({"message": "Response from endpoint2"})

@app.route('/api/endpoint3', methods=['GET'])
def endpoint3():
    time.sleep(2)
    return jsonify({"message": "Response from endpoint3"})

@app.route('/api/endpoint4', methods=['GET'])
def endpoint4():
    time.sleep(2)
    return jsonify({"message": "Response from endpoint4"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
