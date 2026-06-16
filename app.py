import streamlit as st
from mock_ira import get_ira_response  # Use mock for now

st.title("🧠 IRABrain")

goal = st.text_input("Your goal?")

if goal:
    st.info("💙 Processing...")
    
    # Use MOCK response (no API needed!)
    ira_response = get_ira_response(goal)
    
    st.success("💚 Goal set!")
    st.write("**IRA says:**")
    st.write(ira_response)