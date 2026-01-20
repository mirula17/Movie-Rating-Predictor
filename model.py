import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load dataset
data_path = os.path.join(BASE_DIR, "movies.csv")
data = pd.read_csv(data_path)

data = data[['genre', 'year', 'runtime', 'rating']].dropna()

X = data[['genre', 'year', 'runtime']]
y = data['rating']

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('genre', OneHotEncoder(handle_unknown='ignore'), ['genre']),
        ('num', 'passthrough', ['year', 'runtime'])
    ]
)

# Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train model
model.fit(X, y)

# ✅ THIS FUNCTION MUST EXIST
def predict_rating(genre, year, runtime):
    input_data = pd.DataFrame({
        'genre': [genre],
        'year': [year],
        'runtime': [runtime]
    })
    return model.predict(input_data)[0]
