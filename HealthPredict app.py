
import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
model = load("trained_model.joblib")

def show_dashboard():
    st.title("Disease Outbreak Prediction Dashboard")
    st.write("Enter data for prediction")

# Run the Streamlit app
if _name_ == "_main_":
    show_dashboard()
