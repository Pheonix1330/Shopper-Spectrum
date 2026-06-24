import streamlit as st
import joblib

# Load Product Similarity Matrix
product_similarity_df = joblib.load(
    "models/product_similarity.pkl"
)

def recommend_products(product_name, top_n=5):

    if product_name not in product_similarity_df.columns:
        return []

    similar_products = (
        product_similarity_df[product_name]
        .sort_values(ascending=False)
        .iloc[1:top_n+1]
    )

    return similar_products.index.tolist()

def show_recommendation():

    st.title("🎁 Product Recommendation System")

    selected_product = st.selectbox(
        "Select Product",
        product_similarity_df.columns
    )

    if st.button("Get Recommendations"):

        recommendations = recommend_products(
            selected_product
        )

        st.success(
            f"Top 5 Similar Products for '{selected_product}'"
        )

        for product in recommendations:
            st.info(product)