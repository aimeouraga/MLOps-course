# test_main.py

from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app from your main application

# Create a TestClient instance
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "up and running"}

# def test_predict_valid_model():
#     response = client.get("/predict/", params={
#         "model_name": "logistic", 
#         "sepal_length": 5.1, 
#         "sepal_width": 3.5, 
#         "petal_length": 1.4, 
#         "petal_width": 0.2
#     })
#     assert response.status_code == 200
#     assert "prediction" in response.json()

# def test_predict_invalid_model():
#     response = client.get("/predict/", params={
#         "model_name": "invalid_model",
#         "sepal_length": 5.1, 
#         "sepal_width": 3.5, 
#         "petal_length": 1.4, 
#         "petal_width": 0.2
#     })
#     assert response.status_code == 200
#     assert response.json() == {"error": "Model 'invalid_model' not found"}
