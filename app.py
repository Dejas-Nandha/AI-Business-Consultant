import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
import re

st.markdown("""
<style>

/* Remove top white space */
.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}


/* Hide Footer */
footer{
    visibility:hidden;
}

/* Page Background */
.stApp{
    background:#0F172A;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD GEMINI API
# --------------------------------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-3.6-flash")

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Business Consultant",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

/* ================================
   GLOBAL APP
================================ */

.stApp{
    background:#0F172A;
    color:#FFFFFF;
}

/* Remove top padding */
.block-container{
    max-width:1100px;
    padding-top:1rem;
    padding-bottom:2rem;
}

/* Hide Footer */
footer{
    visibility:hidden;
}

/* ================================
   TITLES
================================ */

h1,h2,h3,h4{
    color:white;
    text-align:center;
}

.subtitle{
    text-align:center;
    color:#94A3B8;
    margin-bottom:25px;
}

/* ================================
   CARDS
================================ */

.upload-box,
.answer-box{

    background:#1E293B;

    border-radius:15px;

    padding:20px;

    border:1px solid #334155;

    margin-top:20px;

    margin-bottom:20px;

}

/* ================================
   BUTTON
================================ */

.stButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    padding:0.6rem 1.5rem;

    font-weight:bold;

}

.stButton>button:hover{

    background:#1D4ED8;

    color:white;

}

/* ================================
   TEXT INPUTS
================================ */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stDateInput input{

    background:#1E293B !important;

    color:white !important;

    border:1px solid #334155 !important;

    border-radius:10px !important;

}

/* Placeholder */

input::placeholder{

    color:#CBD5E1 !important;

    opacity:1;

}

textarea::placeholder{

    color:#CBD5E1 !important;

}

/* ================================
   SELECTBOX
================================ */

div[data-baseweb="select"]>div{

    background:#1E293B !important;

    color:white !important;

    border:1px solid #334155 !important;

}

/* Dropdown options */

div[role="listbox"]{

    background:#1E293B !important;

    color:white !important;

}

/* ================================
   FILE UPLOADER
================================ */

[data-testid="stFileUploader"]{
    background:#1E293B !important;
    border:1px solid #334155 !important;
    border-radius:15px !important;
    padding:15px !important;
}

/* Upload area */
[data-testid="stFileUploader"] section{
    background:#1E293B !important;
    border:none !important;
}

/* "Browse files" button */
[data-testid="stFileUploader"] button{
    background:#2563EB !important;
    color:white !important;
    border:none !important;
    border-radius:8px !important;
}

/* Button hover */
[data-testid="stFileUploader"] button:hover{
    background:#1D4ED8 !important;
    color:white !important;
}

/* "Drag and drop file here" / "200MB per file" */
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] div{
    color:white !important;
}

/* ================================
   DATAFRAME
================================ */

[data-testid="stDataFrame"]{

    border-radius:12px;

    overflow:hidden;

}

/* ================================
   SIDEBAR
================================ */

[data-testid="stSidebar"]{

    background:#111827;

}

[data-testid="stSidebar"] *{

    color:white !important;

}

/* ================================
   METRICS
================================ */

[data-testid="metric-container"]{

    background:#1E293B;

    border-radius:12px;

    border:1px solid #334155;

    padding:15px;

}

/* ================================
   TABS
================================ */

button[data-baseweb="tab"]{

    color:white;

}

button[data-baseweb="tab"][aria-selected="true"]{

    background:#2563EB;

    border-radius:8px;

}

/* ================================
   EXPANDER
================================ */

.streamlit-expanderHeader{

    color:white;

}

/* ================================
   SCROLLBAR
================================ */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#334155;

    border-radius:20px;

}

::-webkit-scrollbar-track{

    background:#0F172A;

}

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("<h1>🤖 AI Business Consultant</h1>", unsafe_allow_html=True)

st.markdown(
    "<p class='subtitle'>Upload your business dataset and ask questions in natural language.</p>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

df = None

if uploaded_file:

    try:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        else:
            df = pd.read_excel(uploaded_file)

        st.success("Dataset uploaded successfully.")

        st.subheader("Dataset Preview")

        st.dataframe(df.head(), use_container_width=True)

    except Exception as e:

        st.error(f"Unable to read file.\n\n{e}")

# --------------------------------------------------
# QUESTION
# --------------------------------------------------

question = st.text_input(
    "Ask a business question",
    placeholder="Example: Which region has the highest sales?"
)

ask = st.button("Ask AI")

if ask:

    if df is None:
        st.warning("Please upload a dataset first.")

    elif question.strip() == "":
        st.warning("Please enter a business question.")

    else:

        with st.spinner("🧠 AI is analyzing your dataset..."):

            columns = list(df.columns)

            code_prompt = f"""
You are a Python Pandas expert.

The dataframe is named df.

Dataset columns:
{columns}

Generate ONLY ONE line of Python Pandas code.

Rules:
- Return ONLY executable Python code.
- Do NOT use print().
- Do NOT use markdown.
- Do NOT use ```python.
- The last expression must evaluate to the answer.
- Use only the dataframe df.

Examples:

Question:
List vehicle types

Answer:
df["Vehicle_Type"].dropna().unique()

Question:
Average Sales

Answer:
df["Sales"].mean()

Question:
Top 5 customers by revenue

Answer:
df.sort_values("Revenue", ascending=False).head(5)

User Question:
{question}
"""

            try:

                code_response = model.generate_content(code_prompt)

                generated_code = code_response.text.strip()

                generated_code = re.sub(r"```python", "", generated_code)
                generated_code = re.sub(r"```", "", generated_code).strip()

                st.expander("Generated Pandas Code").code(generated_code)

                result = eval(generated_code)

                explanation_prompt = f"""
You are a Business Data Analyst.

Question:
{question}

Result:
{result}

Explain the result professionally.
"""

                final_response = model.generate_content(explanation_prompt)

                st.markdown("---")
                st.subheader("🤖 AI Business Consultant")

                st.markdown(final_response.text)

                st.subheader("📊 Result")

                if hasattr(result, "to_frame"):
                    st.dataframe(result)

                elif hasattr(result, "head"):
                    st.dataframe(result)

                else:
                    st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")

# ======================================================
# FOOTER
# ======================================================

st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 12px;
    right: 20px;
    font-size: 13px;
    color: #94A3B8;
    z-index: 999;
}
</style>

<div class="footer">
    © 2026 AI Business Consultant | Developed by <b>Dejaswini </b>
</div>
""", unsafe_allow_html=True)