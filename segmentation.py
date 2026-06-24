import streamlit as st
import joblib
import numpy as np

# Load Models
kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def show_segmentation():

    st.title("📊 Customer Segmentation")

    recency = st.number_input(
        "Recency (days since last purchase)",
        min_value=0,
        value=30
    )

    frequency = st.number_input(
        "Frequency (number of purchases)",
        min_value=1,
        value=1
    )

    monetary = st.number_input(
        "Monetary (total spend)",
        min_value=0.0,
        value=100.0
    )

    if st.button("Predict Segment"):

        data = np.array([[recency, frequency, monetary]])

        scaled_data = scaler.transform(data)

        cluster = kmeans.predict(scaled_data)[0]

        cluster_names = {
            0: "High Value Customer",
            1: "At Risk Customer",
            2: "VIP Customer",
            3: "Regular Customer"
        }

        st.success(
            f"Customer Segment: {cluster_names.get(cluster, 'Unknown')}"
        )