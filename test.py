import joblib

# Load your model
model = joblib.load(r'model\heart_model.pkl')

# If you used sklearn's LogisticRegression, print feature names
if hasattr(model, 'feature_names_in_'):
    print("Model's expected features:")
    print(model.feature_names_in_)