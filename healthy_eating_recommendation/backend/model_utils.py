import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset and preprocessed data
df = pd.read_csv("../healthy_eating_recommendation/df_balanced_recipe.csv", low_memory=False) # Change to your respective dirtectory
numerical_cols = ["rating", "calories", "protein", "fat", "sodium"]
X = df[numerical_cols].fillna(df[numerical_cols].mean())

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Load trained MLNN model
mlnn_model = load_model("../backend/mlnn_model.keras")

# Recommendation logic
def recommend(user_input):
    user_input_scaled = scaler.transform(np.array(user_input).reshape(1, -1)).flatten()

    similarity_scores = cosine_similarity(X_scaled, user_input_scaled.reshape(1, -1)).flatten()

    rule_scores = np.array([
        max(0, 1 - (max(0, row[1] - 400) / 400) - (max(0, row[4] - 200) / 200) - (max(0, row[3] - 15) / 15))
        for row in X_scaled
    ])
    rule_scores = np.clip(rule_scores, 0, 1)

    final_scores = (0.7 * similarity_scores) + (0.3 * rule_scores)
    top_indices = np.argsort(final_scores)[::-1][:10]
    return df.iloc[top_indices][["title", "rating", "calories", "protein", "fat", "sodium"]]
