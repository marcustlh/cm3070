# CM3070 - Deep Learning for Healthy Eating Recommendations Using Nutrition Data
This final-year university project is titled "Deep Learning for Healthy Eating Recommendations Using Nutrition Data", developed by Marcus Tan Lai He. It leverages a Multi-Layer Neural Network (MLNN) model integrated with natural language processing to recommend healthier food choices based on structured nutritional data.

## Project Overview
This project builds a hybrid recommendation engine that combines:
- Content-based filtering using cosine similarity on nutritional data.
- Rule-based filtering to enforce dietary limits (calories, fat, sodium).
- A deep learning (MLNN) model trained on nutritional and ingredient data to enhance dietary relevance.

## Technologies Used
- Python 3.10
- TensorFlow / Keras 3
- Flask (Backend API)
- Streamlit (Frontend UI)
- Scikit-learn, NumPy, Pandas

## Dataset
- Source: https://www.kaggle.com/datasets/hugodarwood/epirecipes
- Processed file: df_balanced_recipe.csv

## How to Run the Project Locally
1. Clone the repository
   git clone https://github.com/your-username/healthy_eating_recommendation.git
   cd healthy_eating_recommendation

2. Install dependencies
   pip install -r requirements.txt

3. Run the backend (Flask)
   cd backend
   python app.py

4. Run the frontend (Streamlit)
   *In a separate terminal*
   cd frontend
   streamlit run streamlit_app.py

# License
This project is intended for educational and research purposes.
