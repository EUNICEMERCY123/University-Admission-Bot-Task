print(" Welcome to the University Admissions Bot")
print("Ask about eligibility, documents, deadlines, fees")
print("Type 'ug checklist' or 'pg checklist'")
print("Type 'exit' to quit\n")

admission_info = {
    "eligibility": "UG requires 10+2 completion. PG requires a relevant bachelor's degree.",
    "documents": "Mark sheets, ID proof, passport-size photos, and application form.",
    "deadline": "Admission deadlines usually fall between March and July.",
    "application process": "Apply online, upload documents, pay the application fee.",
    "fees": "Application fees depend on the university and course."
}

def checklist(program):
    if program == "ug":
        return """
UG ADMISSION CHECKLIST (Compressed):
- Eligibility: 10+2 passed
- Documents: 12th mark sheet, ID proof
- Entrance Exam: As per university
- Deadline: March–July
"""
    elif program == "pg":
        return """
PG ADMISSION CHECKLIST (Compressed):
- Eligibility: UG degree
- Documents: Degree certificate, transcripts
- Entrance Exam: University specific
- Deadline: March–July
"""
    else:
        return "Invalid checklist request."

while True:
    user_input = input("Ask a question: ").lower()

    if user_input == "exit":
        print("Thank you for using the University Admissions Bot!")
        break

    elif "ug checklist" in user_input:
        print(checklist("ug"))

    elif "pg checklist" in user_input:
        print(checklist("pg"))

    elif "eligibility" in user_input:
        print(admission_info["eligibility"])

    elif "document" in user_input:
        print(admission_info["documents"])

    elif "deadline" in user_input:
        print(admission_info["deadline"])

    elif "process" in user_input or "apply" in user_input:
        print(admission_info["application process"])

    elif "fee" in user_input:
        print(admission_info["fees"])

    else:
        print("I can help with eligibility, documents, deadlines, fees, or checklists.")
