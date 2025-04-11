from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import psycopg2
import os
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# ----- Task 5: Connect to PostgreSQL -----
@app.route('/db')
def db_status():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DB', 'mydb'),
            user=os.getenv('POSTGRES_USER', 'myuser'),
            password=os.getenv('POSTGRES_PASSWORD', 'mypassword'),
            host='postgres',
            port='5432'
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL: {version}"
    except Exception as e:
        return f"DB Error: {str(e)}"

# ----- Task 8: Load ML Model -----
iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})

# ----- Task 1: Basic Flask Home Route -----
@app.route('/')
def home():
    return "DevOps Project: Flask + Prometheus + PostgreSQL + ML API"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
