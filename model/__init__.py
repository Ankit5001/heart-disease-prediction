
from .predictor import HeartPredictor

# Package metadata
__version__ = '1.0.0'
__author__ = 'Sachin and Ankit'

# Model configuration
MODEL_CONFIG = {
    'model_path': 'model/heart_model.joblib',
    'features': [
        'Age', 'Sex', 'ChestPainType', 'Cholesterol',
        'FastingBS', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'
    ],
    'categorical_features': ['Sex', 'ChestPainType', 'ExerciseAngina', 'ST_Slope'],
    'numeric_features': ['Age', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']
}

# Feature mappings
FEATURE_MAPPINGS = {
    'Sex': {'Male': 1, 'Female': 0},
    'ExerciseAngina': {'Yes': 1, 'No': 0},
    'ChestPainType': ['TA', 'ATA', 'NAP', 'ASY'],
    'ST_Slope': ['Up', 'Flat', 'Down']
}

# Export symbols
__all__ = [
    'HeartPredictor',
    'MODEL_CONFIG',
    'FEATURE_MAPPINGS',
    '__version__',
    '__author__'
]