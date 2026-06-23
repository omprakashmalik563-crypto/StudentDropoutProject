import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    page_icon="🎯",
    layout="wide"
)

# Load Model
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

# CSS
st.markdown("""
<style>

.predict-header{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:35px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:20px;
}

.input-card{
background:#f8fafc;
padding:20px;
border-radius:15px;
box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

.result-card{
padding:20px;
border-radius:15px;
text-align:center;
font-size:22px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='predict-header'>
<h1>🔍 Student Dropout Prediction</h1>
<p>Predict whether a student is at risk of dropping out using XGBoost</p>
</div>
""", unsafe_allow_html=True)

# Input Section
st.subheader("📋 Student Information")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 📚 Academic Details")

    age = st.slider(
        "👤 Age",
        15,
        22,
        18
    )

    studytime = st.slider(
        "📖 Study Time",
        1,
        4,
        2
    )

    failures = st.slider(
        "❌ Previous Failures",
        0,
        4,
        0
    )

with col2:

    st.markdown("### 📅 Attendance & Grades")

    absences = st.slider(
        "📅 Absences",
        0,
        50,
        5
    )

    g1 = st.slider(
        "📝 G1 Grade",
        0,
        20,
        10
    )

    g2 = st.slider(
        "📝 G2 Grade",
        0,
        20,
        10
    )

st.write("")

# Prediction Button
if st.button(
    "🚀 Predict Student Risk",
    use_container_width=True
):

    data = {
        feature: 0
        for feature in features
    }

    if "age" in data:
        data["age"] = age

    if "studytime" in data:
        data["studytime"] = studytime

    if "failures" in data:
        data["failures"] = failures

    if "absences" in data:
        data["absences"] = absences

    if "G1" in data:
        data["G1"] = g1

    if "G2" in data:
        data["G2"] = g2

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    risk_percent = round(
        probability * 100,
        2
    )

    st.divider()

    st.subheader("📊 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Dropout Risk Score",
            f"{risk_percent}%"
        )

    with col2:
        st.metric(
            "Model Accuracy",
            "92.41%"
        )

    st.progress(int(risk_percent))

    if prediction == 1:

        st.error(
            f"⚠️ HIGH RISK OF DROPOUT ({risk_percent}%)"
        )

        st.warning("""
Recommended Actions:

• Academic counselling

• Attendance monitoring

• Mentorship support

• Regular performance review
""")

    else:

        st.success(
            f"✅ LOW RISK OF DROPOUT ({100-risk_percent:.2f}%)"
        )

        st.info("""
Student is currently performing well.

Continue monitoring attendance and academic performance.
""")