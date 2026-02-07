print(" Welcome to the University Admissions Bot")
print("Type 'exit' to quit\n")

admission_info = {
    "eligibility": "Eligibility usually requires completion of 12th grade for UG and a bachelor's degree for PG programs.",
    "documents": "Common documents include mark sheets, ID proof, passport-size photos, and application forms.",
    "deadline": "Admission deadlines vary by university but usually fall between March and July.",
    "application process": "The application process includes filling out the online form, uploading documents, and paying the application fee.",
    "fees": "Application fees depend on the university and course selected."
}

while True:
    user_input = input("Ask a question about admissions: ").lower()

    if user_input == "exit":
        print("Thank you for using the University Admissions Bot!")
        break

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
        print("Sorry, I can help with eligibility, documents, deadlines, fees, and application process.")
