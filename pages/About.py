import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="👨‍💻",
    layout="wide"
)

# ==========================
# Custom CSS
# ==========================

st.markdown("""
<style>

.hero{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:40px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:25px;
}

.dev-card{
background:#f8fafc;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0px 2px 8px rgba(0,0,0,0.1);
margin-bottom:15px;
}

.footer{
text-align:center;
padding:20px;
color:gray;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.markdown("""
<div class="hero">

<h1>👨‍💻 About The Project</h1>

<p>
Student Dropout Prediction System
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# Project Description
# ==========================

st.subheader("📖 Project Overview")

st.write("""
The Student Dropout Prediction System is a Machine Learning project
developed to identify students who are at risk of dropping out.

The project uses academic performance, attendance records and
student information to predict dropout risk.

An XGBoost Machine Learning model is used to generate predictions
with high accuracy.
""")

st.divider()

# ==========================
# Technologies Used
# ==========================

st.subheader("🛠 Technologies Used")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🐍 Python")

with col2:
    st.info("📊 Streamlit")

with col3:
    st.info("🤖 XGBoost")

with col4:
    st.info("📈 Scikit-Learn")

st.divider()

# ==========================
# Project Statistics
# ==========================

st.subheader("📊 Project Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🎯 Accuracy: 92.41%")

with col2:
    st.success("📚 Dataset: 395 Students")

with col3:
    st.success("🤖 Model: XGBoost")

st.divider()

# ==========================
# Development Team
# ==========================

st.subheader("👨‍💻 Development Team")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="dev-card">
    <h3>Amlan Kumar Biswal</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dev-card">
    <h3>Ritesh Rohan</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dev-card">
    <h3>Ipshita Mishra</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="dev-card">
    <h3>Rachita Swain</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dev-card">
    <h3>Priyanshu Priyadarshani Choudhury</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

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