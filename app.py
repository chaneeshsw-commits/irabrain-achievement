import streamlit as st
from mock_ira import get_ira_response  # Use mock for now
from animations import show_loading_animation, show_success_animation
from database import save_goal,get_goals

st.title("🧠 IRABrain")

goal = st.text_input("Your goal?")

if goal:

     # BLUE ANIMATION (new!)
    show_loading_animation()
    st.info("💙 Processing...")
    
    # Use MOCK response (no API needed!)
    #save to database
    save_goal(goal)

    ira_response = get_ira_response(goal)
    show_success_animation()
    st.write(ira_response)
     # GREEN ANIMATION (new!)
    
    

    #show all goals
    st.subheader("your Goals:")
    for g in get_goals():
        st.write(f"{g.goal}")

    
    
    
   