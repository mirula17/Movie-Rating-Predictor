import streamlit as st
from model import predict_rating

st.set_page_config(page_title="Movie Rating Predictor")

st.title("🎬 Movie Rating Predictor")

genre = st.selectbox(
    "Select Genre",
    ["Action", "Drama", "Comedy", "Romance", "Thriller"]
)

year = st.number_input(
    "Release Year",
    min_value=1950,
    max_value=2025,
    value=2020
)

runtime = st.number_input(
    "Runtime (minutes)",
    min_value=60,
    max_value=240,
    value=120
)

if st.button("Predict Rating"):
    rating = predict_rating(genre, year, runtime)
    st.success(f"⭐ Predicted Rating: {round(rating, 1)} / 10")
