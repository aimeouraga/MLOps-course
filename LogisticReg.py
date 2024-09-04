from Irisdataset import X, y
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

print(X_train)

model = LogisticRegression(max_iter=300)
model.fit(X_train, y_train)
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)
print(accuracy)