import streamlit as st

st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# Custom CSS
# ==========================

st.markdown("""
<style>

.hero{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:60px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:25px;
}

.metric-box{
background:#1a1a2e;
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0px 4px 15px rgba(0,0,0,0.3);
margin-bottom:10px;
color:#ffffff !important;
border:1px solid rgba(255,255,255,0.1);
}

.metric-box h4{
color:#a78bfa !important;
}

.metric-box h1{
color:#ffffff !important;
}

.metric-box p{
color:#cccccc !important;
}

.footer{
text-align:center;
padding:25px;
border-radius:15px;
background:#1a1a2e;
color:#cccccc;
margin-top:20px;
border:1px solid rgba(255,255,255,0.1);
}

.footer h3{
color:#ffffff;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Hero Section
# ==========================

st.markdown("""
<div class='hero'>

<h1>🎓 Student Dropout Prediction System</h1>

<h3>XGBoost Based Machine Learning Project</h3>

<p>
Predict students who are at risk of dropping out based on
academic performance, attendance patterns and demographic data.
</p>

<br>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
🤖 ML Powered
</span>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
📊 XGBoost
</span>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
🎯 92.41% Accuracy
</span>

</div>
""", unsafe_allow_html=True)

# ==========================
# Metrics Cards
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-box">
    <h4>🎯 Accuracy</h4>
    <h1>92.41%</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
    <h4>📚 Dataset</h4>
    <h1>395</h1>
    <p>Students</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
    <h4>🤖 Model</h4>
    <h1>XGBoost</h1>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================
# Features
# ==========================

st.subheader("📌 Project Features")

col1, col2 = st.columns(2)

with col1:
    st.success("Student Risk Prediction")
    st.success("Interactive Dashboard")
    st.success("Attendance Analysis")

with col2:
    st.success("Feature Importance Analysis")
    st.success("XGBoost Machine Learning Model")
    st.success("Streamlit Web Application")

st.divider()

# ==========================
# About Project
# ==========================

st.subheader("📖 About Project")

st.write("""
This machine learning project predicts whether a student is at risk of dropping out.

The model is trained using academic performance, attendance records,
and demographic information.

Educational institutions can use this system for early intervention,
helping students improve their academic outcomes.
""")

st.divider()

# ==========================
# Project Statistics
# ==========================

st.subheader("📊 Project Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🎓 395 Students")

with col2:
    st.info("📈 32 Features")

with col3:
    st.info("🤖 XGBoost Model")

with col4:
    st.info("🚀 Live Deployment")

st.divider()

# ==========================
# Footer
# ==========================

st.markdown("""
<div class="footer">

<h3>🎓 Student Dropout Prediction System</h3>

<p>
Built using Python, Streamlit, Scikit-Learn and XGBoost
</p>


<p>
Made with ❤️ for Machine Learning & Educational Analytics
</p>

</div>
""", unsafe_allow_html=True)