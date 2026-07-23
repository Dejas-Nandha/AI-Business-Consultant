import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
}

/* Main Title */
.title{
    font-size:38px;
    font-weight:700;
    color:white;
    display:flex;
    align-items:center;
    gap:12px;
    margin-bottom:8px;
}

/* Subtitle */
.subtitle{
    color:#94A3B8;
    font-size:18px;      /* Increased from 17px */
    margin-bottom:30px;
}

/* Section Heading */
.section{
    font-size:22px;
    font-weight:600;
    color:white;
    margin-top:15px;
    margin-bottom:15px;
}

/* Card */
.card{
    background:#1E293B;
    border:1px solid rgba(255,255,255,0.08);
    border-radius:16px;
    padding:20px;
    margin-bottom:18px;
    height:100%;
}

/* Card Title */
.card h4{
    margin-top:0;
    color:white;
}

/* Card Text */
.card p{
    color:#CBD5E1;
    font-size:15px;
    line-height:1.8;
}

/* Small Text */
.small{
    color:#CBD5E1;
    font-size:16px;
    line-height:1.7;
}

/* Footer */
.footer{
    text-align:center;
    color:#94A3B8;
    font-size:14px;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<h1 class="title">ℹ️ About AI Business Consultant</h1>

<div class="subtitle">
Empowering smarter business decisions through AI-driven data analysis.
</div>
""", unsafe_allow_html=True)
# =====================================================
# TOP METRICS
# =====================================================

m1, m2, m3 = st.columns(3)

m1.metric("Mission", "AI Analytics")
m2.metric("AI Engine", "Gemini")
m3.metric("Version", "v1.0")

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.markdown('<div class="section">🚀 Project Overview</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">

<p>

AI Business Consultant is an intelligent analytics platform that allows users to upload business datasets and interact with them using natural language.

Instead of manually writing SQL queries or Python code, users simply ask questions about their data. Google Gemini AI interprets the request, generates Pandas-based analysis, and provides meaningful business insights in seconds.

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# FEATURE CARDS
# =====================================================

st.markdown('<div class="section">✨ Platform Highlights</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
<div class="card">

<h4>📂 Smart Data Upload</h4>

<p>

• Upload CSV & Excel files

• Automatic validation

• Instant preview

• Ready for analysis

</p>

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="card">

<h4>🤖 AI Analysis</h4>

<p>

• Google Gemini AI

• Natural language queries

• AI-generated Pandas analysis

• Instant responses

</p>

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="card">

<h4>📈 Business Insights</h4>

<p>

• KPI discovery

• Trend analysis

• Data profiling

• Business recommendations

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# WORKFLOW
# =====================================================

st.markdown('<div class="section">⚙️ How It Works</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">

<p>

📂 Upload Dataset

⬇️

🧹 Validate & Prepare Data

⬇️

🤖 Google Gemini AI Analysis

⬇️

💬 Ask Business Questions

⬇️

📊 Generate Pandas Analysis

⬇️

📈 Business Insights & Recommendations
</p>

</div>
""", unsafe_allow_html=True)
# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.markdown('<div class="section">🛠 Technology Stack</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)

with t1:
    st.metric("Frontend", "Streamlit")

with t2:
    st.metric("Backend", "Python")

with t3:
    st.metric("AI", "Gemini")

st.markdown("")

st.markdown("""
<div class="card">

<p>

🐍 Python

📊 Pandas

⚡ Streamlit

🤖 Google Gemini AI

📂 OpenPyXL

🔐 Python-dotenv

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# WHY THIS PLATFORM
# =====================================================

st.markdown('<div class="section">🎯 Why AI Business Consultant?</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    st.markdown("""
<div class="card">

<h4>Business Value</h4>

<p>

✔ Faster decision making

✔ AI-powered analytics

✔ Interactive data exploration

✔ Reduced manual effort

</p>

</div>
""", unsafe_allow_html=True)

with right:

    st.markdown("""
<div class="card">

<h4>Ideal For</h4>

<p>

✔ Business Analysts

✔ Students

✔ Data Analysts

✔ Small & Medium Businesses

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# DEVELOPER
# =====================================================

st.markdown('<div class="section">👩‍💻 Developer</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h4>Dejaswini G</h4>

<p>

Aspiring Data Analyst

Passionate about Business Analytics, Artificial Intelligence,
Python Development, Data Visualization and Business Intelligence.

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

AI Business Consultant • Powered by Python, Streamlit & Google Gemini AI

</div>
""", unsafe_allow_html=True)