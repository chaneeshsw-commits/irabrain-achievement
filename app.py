import streamlit as st
from mock_ira import get_ira_response  # Use mock for now
from animations import show_loading_animation, show_success_animation
from database import save_goal, get_goals, log_completion, log_missed

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

st.subheader("your Goals:")
for g in get_goals():
    col1,col2,col3  =st.columns([2,1,1])
    with col1:
        st.write(f" {g.goal} | streak: {g.streak}")
        with col2:
            if st.button(f"✅", key=f"done_{g.goal}"):
                log_completion(g.goal)
                st.rerun()

    with col3: 
        if st.button(f"❌", key=f"miss_{g.goal}"):
            reason =st.text_input(f"Why missed?", key =f"reason_{g.goal}")   
            if reason:
                log_missed(g.goal,reason)
                st.warning("No worries! Tomorrow's a fresh start! 💪")
                st.rerun()       

    
    
   