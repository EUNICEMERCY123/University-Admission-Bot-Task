import streamlit as st

st.set_page_config(page_title="University Admissions Bot", page_icon="🎓")

st.title("🎓 University Admissions Bot")
st.write("Get quick, compressed answers about university admissions")

st.divider()

admission_info = {
    "Eligibility": "UG requires 10+2 completion. PG requires a relevant bachelor's degree.",
    "Documents": "Mark sheets, ID proof, passport-size photos, and application form.",
    "Deadlines": "Admission deadlines usually fall between March and July.",
    "Application Process": "Apply online, upload documents, and pay the application fee.",
    "Fees": "Application fees depend on the university and course."
}

st.subheader("📌 Ask about admissions")
option = st.selectbox(
    "Choose a topic",
    ["Eligibility", "Documents", "Deadlines", "Application Process", "Fees"]
)

st.success(admission_info[option])

st.divider()

st.subheader("🧾 Smart Admission Checklist")

program = st.radio("Select program type:", ["UG", "PG"])

if program == "UG":
    st.info("""
    **UG Admission Checklist (Compressed)**
    - Eligibility: 10+2 passed
    - Documents: 12th mark sheet, ID proof
    - Entrance Exam: As per university
    - Deadline: March–July
    """)
else:
    st.info("""
    **PG Admission Checklist (Compressed)**
    - Eligibility: UG degree
    - Documents: Degree certificate, transcripts
    - Entrance Exam: University specific
    - Deadline: March–July
    """)

st.caption("Built for Intel GenAI Challenge 🚀")
