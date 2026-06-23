import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Admin Dashboard",
    layout="wide"
)

st.title("⚙️ Admin Dashboard")

# Load model
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

# Project Summary
st.subheader("📌 Project Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "XGBoost")

with col2:
    st.metric("Accuracy", "92.41%")

with col3:
    st.metric("Features", len(features))

st.divider()

# Feature Importance
st.subheader("📊 Feature Importance")

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

st.dataframe(
    importance_df.head(10),
    use_container_width=True
)

# Chart
fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    importance_df["Feature"][:10],
    importance_df["Importance"][:10]
)

plt.xticks(rotation=45)

st.pyplot(fig)

st.divider()

# Top Risk Factors
st.subheader("🚨 Top Risk Factors")

for i, row in importance_df.head(5).iterrows():
    st.write(
        f"✅ {row['Feature']} → Importance: {row['Importance']:.4f}"
    )

st.divider()

# Model Notes
st.subheader("📝 Model Notes")

st.info("""
This model uses XGBoost Classification
to predict students at risk of dropping out.

Higher importance features have
greater impact on predictions.
""")