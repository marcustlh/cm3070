import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/recommend"

st.set_page_config(page_title="Healthy Recipe Recommender", layout="centered")
st.title("Healthy Eating Recommendation System")

st.sidebar.header("Your Preferences")
rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 4.5)
calories = st.sidebar.slider("Max Calories", 100, 1000, 400)
protein = st.sidebar.slider("Min Protein", 0, 50, 20)
fat = st.sidebar.slider("Max Fat", 0, 50, 10)
sodium = st.sidebar.slider("Max Sodium", 0, 1000, 150)

if st.button("Get Recommendations"):
    preferences = [rating, calories, protein, fat, sodium]
    response = requests.post(API_URL, json={"preferences": preferences})

    if response.status_code == 200:
        results = response.json()
        st.subheader("Top 10 Recommended Recipes")
        for recipe in results:
            st.markdown(f"### {recipe['title']}")
            st.write(f"Rating: {recipe['rating']}")
            st.write(f"Calories: {recipe['calories']}, 🥩 Protein: {recipe['protein']}g, 🧈 Fat: {recipe['fat']}g, 🧂 Sodium: {recipe['sodium']}mg")
            st.markdown("---")
    else:
        st.error("Failed to fetch recommendations. Make sure the Flask API is running.")
