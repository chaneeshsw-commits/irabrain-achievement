def get_ira_response(goal: str):
    """
    Mock IRA responses (hardcoded)
    Replace with real Claude API later
    """
    
    responses = {
        "run": "Running daily? That's POWERFUL! 🏃 Start tomorrow at 7 AM. You've got this! 💪",
        "build": "Building your first app? That's the spirit! 🚀 Start with Day 1 planning today.",
        "learn": "Learning AI? Perfect timing! 📚 Commit 1 hour daily. You'll master it! 🧠",
        "default": "That's an amazing goal! 💜 Let's make it happen together! When can you start?"
    }
    
    goal_lower = goal.lower()
    
    if "run" in goal_lower:
        return responses["run"]
    elif "build" in goal_lower or "app" in goal_lower:
        return responses["build"]
    elif "learn" in goal_lower or "ai" in goal_lower:
        return responses["learn"]
    else:
        return responses["default"]