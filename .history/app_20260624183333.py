import streamlit as st

from segmentation import show_segmentation
from recommendation import show_recommendation

# Page Configuration
st.set_page_config(
    page_title="Retail Customer Segmentation & Recommendation",
    page_icon="🛍️",
    layout="wide"
)

# Sidebar
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Customer Segmentation",
        "Product Recommendation"
    ]
)

# Home Page
if page == "Home":

    st.title("🛍️ Retail Customer Segmentation & Recommendation System")

    st.markdown("---")

    st.subheader("📊 Customer Segmentation")

    st.write("""
    Predict customer segments using RFM Analysis:
    
    - Recency
    - Frequency
    - Monetary
    
    Customer Segments:
    - VIP Customer
    - High Value Customer
    - Regular Customer
    - At Risk Customer
    """)

    st.markdown("---")

    st.subheader("🎁 Product Recommendation System")

    st.write("""
    Recommend products using Item-Based Collaborative Filtering.
    
    Features:
    - Product Similarity Matrix
    - Cosine Similarity
    - Top 5 Product Recommendations
    """)

# Customer Segmentation Page
elif page == "Customer Segmentation":
    show_segmentation()

# Product Recommendation Page
elif page == "Product Recommendation":
    show_recommendation()