from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import mlflow
from sklearn.metrics import accuracy_score
# mlflow.autolog()

# TODO: Setup MLflow.
mlflow.set_tracking_uri("http://127.0.0.1:8080")

mlflow.set_experiment("mflow Autologging start")

# TODO: Setup autologging.
mlflow.autolog()

db = load_diabetes()

X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# Create and train models
rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
rf.fit(X_train, y_train)

# Use the model to make predictions on the test dataset
predictions = rf.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(accuracy)
