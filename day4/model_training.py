from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import pickle

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train Logistic Regression model
logreg_model = LogisticRegression(max_iter=200)
logreg_model.fit(X, y)

# Train Random Forest model
rf_model = RandomForestClassifier()
rf_model.fit(X, y)

# TODO: Save logistic regression model to disk.
with open('logreg_model.pkl', 'wb') as file:
    pickle.dump(logreg_model, file)

# TODO: Save random forest model to disk.
with open('rf_model.pkl', 'wb') as file:
    pickle.dump(rf_model, file)
