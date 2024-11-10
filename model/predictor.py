# For prediction
import pandas as pd
import joblib
class HeartPredictor:
    def __init__(self):
        self.pipeline = joblib.load(r'model/heart_model1.pkl')
        
    def predict(self, features):
        df = pd.DataFrame([features])
        return self.pipeline.predict(df)[0]
    
    def predict_proba(self, features):
        df = pd.DataFrame([features])
        proba = self.pipeline.predict_proba(df)[0]
        return round(max(proba) * 100, 2)
