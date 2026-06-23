import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

df = pd.read_csv("data/student_data.csv", sep=";")

st.title("📊 Student Analytics Dashboard")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👨‍🎓 Total Students", len(df))

with col2:
    st.metric("📚 Avg Final Grade", round(df["G3"].mean(), 2))

with col3:
    st.metric("❌ Avg Absences", round(df["absences"].mean(), 2))

with col4:
    st.metric("⚠️ Total Failures", int(df["failures"].sum()))

st.divider()

# Grade Distribution
st.subheader("📈 Grade Distribution")

fig1 = px.histogram(
    df,
    x="G3",
    nbins=20,
    title="Final Grade Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# Failure Distribution
st.subheader("📉 Failure Distribution")

failure_df = df["failures"].value_counts().reset_index()
failure_df.columns = ["Failures", "Students"]

fig2 = px.bar(
    failure_df,
    x="Failures",
    y="Students",
    title="Students by Failure Count"
)

st.plotly_chart(fig2, use_container_width=True)

# Risk Analysis
risk_students = len(df[df["G3"] < 10])
safe_students = len(df[df["G3"] >= 10])

st.subheader("🎯 Risk Analysis")

fig3 = px.pie(
    values=[risk_students, safe_students],
    names=["At Risk", "Safe"],
    title="Student Risk Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# Dataset Preview
st.subheader("📋 Dataset Preview")

st.dataframe(df.head(10))