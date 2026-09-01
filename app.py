import streamlit as st

import pandas as pd
import pickle
from pickle import load


# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Bankruptcy Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Bankruptcy Prevention")

@st.cache_resource
def load_files():
    lr_model = pickle.load(
    open("lr.pkl", "rb"))
    return lr_model

    
features = [
    "industrial_risk",
    "management_risk",
    "financial_flexibility",
    "credibility",
    "competitiveness",
    "operating_risk"
]
allowed_values = [0, 0.5, 1]
cols = st.columns(3)
input ={}

for i,feature in enumerate(features):
      with cols[i%3]:
           input[feature] = st.radio(feature.replace("_"," ").title() , allowed_values ,horizontal=True)
input_df = pd.DataFrame([input])

st.sidebar.header("About")

st.sidebar.info(
    """
    Bankruptcy Prediction App

    Logistic Regression Model
    """
)


st.subheader("Input Summary")
st.dataframe(input, use_container_width=True)

model = load_files()



with st.form("prediction_form"):
    # input widgets

    submitted = st.form_submit_button("Predict")
    st.spinner()
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

st.metric("Probability of Bankruptcy", f"{probability[1]*100:.2f}%")


if prediction == 0:
    with st.spinner("Predicting..."):
       st.success("✅ Low Risk")
    
       st.write("The company is unlikely to go bankrupt.")
else:
    with st.spinner("Predicting..."):
        st.error("⚠ High Risk")
        st.write("The company has a higher probability of bankruptcy.")

st.markdown("""
<style>
div.stButton > button {
    width:100%;
    height:55px;
    background:#2E8B57;
    color:white;
    border-radius:8px;
    font-size:18px;
}
div.stButton > button:hover{
    background:#1E6E43;
}
</style>
""", unsafe_allow_html=True)



