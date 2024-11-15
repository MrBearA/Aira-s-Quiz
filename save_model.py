import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load sample data
data = load_iris()
X, y = data.data, data.target

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'model.pkl')
