import streamlit as st
import time

def show_loading_animation():
    """Show blue loading animation"""
    placeholder = st.empty()
    
    # Animate 3 dots
    for i in range(3):
        with placeholder.container():
            st.info("💙 Processing" + "." * (i + 1))
            time.sleep(0.5)
    
    placeholder.empty()

def show_success_animation():
    """Show green success animation"""
    st.success("💚 Goal set! You've got this! 🎯")
    time.sleep(1)
    