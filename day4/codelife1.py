from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sklearn.linear_model import LogisticRegression
import pickle
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field, confloat
import numpy as np
from fastapi import FastAPI, HTTPException
import asyncio



class IrisFeatures(BaseModel):
    sepal_length: float #confloat(gt=0, le=10.0) = Field(..., description="Sepal length in cm (0 < value ≤ 10)")
    sepal_width: float# confloat(gt=0, le=5.0) = Field(..., description="Sepal width in cm (0 < value ≤ 5)")
    petal_length: float #confloat(gt=0, le=7.0) = Field(..., description="Petal length in cm (0 < value ≤ 7)")
    petal_width: float #confloat(gt=0, le=3.0) = Field(..., description="Petal width in cm (0 < value ≤ 3)")

    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

app = FastAPI()

model = {}  # Global variable to store the model

# Define a lifespan context
@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    # Load both models when the app starts
    try:
        with open('logreg_model.pkl', 'rb') as f:
            model['logistic'] = pickle.load(f)
        with open('rf_model.pkl', 'rb') as f:
            model['randomForest'] = pickle.load(f)
        print("Models loaded successfully.")
    except Exception as e:
        print(f"Error loading models: {e}")
    
    yield

    # Cleanup code here if needed when the app shuts down
    print("App is shutting down.")

app.router.lifespan_context = lifespan

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "up and running"}

@app.get("/model_keys")
def model_keys():
    # Display the keys of the model dictionary
    keys = list(model.keys())
    return {"model_keys": keys}


@app.post("/predict/{model_name}")
# async def predict(model_name: str, features: List[float]):
async def predict(model_name: str, features: IrisFeatures):
    global model
    await asyncio.sleep(2) 
    if model_name not in model:
        raise HTTPException(status_code=404, detail="Model not found")
    
    # Get the selected model
    model = model[model_name]

    input_data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])

    
    # Make the prediction
    prediction = model.predict(input_data).tolist()
    
    return {"model": model_name, "prediction": prediction}


