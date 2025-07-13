import streamlit as st
from fuzzywuzzy import fuzz

data = [
    {"question": "What does the eligibility verification agent (EVA) do?", "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."},
    {"question": "What does the claims processing agent (CAM) do?", "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."},
    {"question": "How does the payment posting agent (PHIL) work?", "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."},
    {"question": "Tell me about Thoughtful AI's Agents.", "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."},
    {"question": "What are the benefits of using Thoughtful AI's agents?", "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."}
]

def find_best_match(user_question):
    if not user_question or not user_question.strip():
        return None
    
    best_score = 0
    best_answer = None
    
    for item in data:
        score = fuzz.ratio(user_question.lower(), item["question"].lower())
        if score > best_score:
            best_score = score
            best_answer = item["answer"]
    
    return best_answer if best_score >= 50 else None

def get_fallback_response():
    return "Sorry, I didn't understand your question. You can ask me about EVA (Eligibility Verification Agent), CAM (Claims Processing Agent), PHIL (Payment Posting Agent), or general benefits of our AI agents. Please try rephrasing your question."

st.title("🤖 Thoughtful AI Chatbot")
st.write("Ask me about Thoughtful AI's automation agents!")

user_input = st.text_input("Your question:", placeholder="e.g., What does EVA do?")

if user_input:
    try:
        answer = find_best_match(user_input)
        if answer:
            st.write("**Answer:**")
            st.write(answer)
        else:
            st.write("**Answer:**")
            st.write(get_fallback_response())
    except Exception as e:
        st.write("**Answer:**")
        st.write("I apologize, but I encountered an error. Please try asking your question again.")