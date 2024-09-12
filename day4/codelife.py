# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from sklearn.linear_model import LogisticRegression
# import pickle
# from contextlib import asynccontextmanager

# app = FastAPI()

# model = None  # Global variable to store the model

# # Define a lifespan context
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     global model
#     # Load the model when the app starts
#     with open('logreg_model.pkl', 'rb') as f:
#         model = pickle.load(f)
#     print("Model loaded successfully.")

#     yield

#     # Cleanup code here if needed when the app shuts down
#     print("App is shutting down.")

# app.router.lifespan_context = lifespan

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# @app.get("/predict/")
# def predict(value: float):
#     prediction = model.predict([[value]])  # Assuming the model expects one feature
#     return {"prediction": prediction[0]}

# @app.get("/health")
# def health():
#     return {"status": "up and running"}






# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from sklearn.linear_model import LogisticRegression
# import pickle
# from contextlib import asynccontextmanager

# app = FastAPI()

# model_dict = {}  # Global dictionary to store the model

# # Define a lifespan context
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     global model_dict
#     # Load the model when the app starts
#     with open('logreg_model.pkl', 'rb') as f:
#         model = pickle.load(f)
#         model_dict['model'] = model  # Save the model into the dictionary
#     print("Model loaded successfully.")

#     yield

#     # Cleanup code here if needed when the app shuts down
#     print("App is shutting down.")

# app.router.lifespan_context = lifespan

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# @app.get("/predict/")
# def predict(value: float):
#     model = model_dict.get('model')
#     if model:
#         prediction = model.predict([[value]])  # Assuming the model expects one feature
#         return {"prediction": prediction[0]}
#     return {"error": "Model not loaded"}

# @app.get("/health")
# def health():
#     return {"status": "up and running"}

# @app.get("/model_keys")
# def model_keys():
#     # Display the keys of the model dictionary
#     keys = list(model_dict.keys())
#     return {"model_keys": keys}





from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import pickle
from contextlib import asynccontextmanager
from typing import List

app = FastAPI()

model_dict = {}  # Global dictionary to store the model

# Define a lifespan context
@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_dict
    # Load the model when the app starts
    with open('logreg_model.pkl', 'rb') as f:
        model = pickle.load(f)
        model_dict['model'] = model  # Save the model into the dictionary
    print("Model loaded successfully.")

    yield

    # Cleanup code here if needed when the app shuts down
    print("App is shutting down.")

app.router.lifespan_context = lifespan

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/predict/")
def predict(
    sepal_length: float = Query(..., description="Sepal length in cm"),
    sepal_width: float = Query(..., description="Sepal width in cm"),
    petal_length: float = Query(..., description="Petal length in cm"),
    petal_width: float = Query(..., description="Petal width in cm")
):
    model = model_dict.get('model')
    if model:
        features = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(features)  # Assuming the model expects four features
        return {"prediction": prediction[0]}
    return {"error": "Model not loaded"}

@app.get("/health")
def health():
    return {"status": "up and running"}

@app.get("/model_keys")
def model_keys():
    # Display the keys of the model dictionary
    keys = list(model_dict.keys())
    return {"model_keys": keys}




