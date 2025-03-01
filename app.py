import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model_path = "security.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("Cyber Attack Detection")

user_input = st.text_area("Enter numerical values separated by commas:")

if st.button("Classify"):
    input_values = [float(value.strip()) for value in user_input.split(",")]
    df = pd.DataFrame([input_values])
    result = model.predict(df)[0]
    if result == 1:
        st.success("Prediction: This is an Attack!")
    else:
        st.error("Prediction: This is Normal Traffic!")
