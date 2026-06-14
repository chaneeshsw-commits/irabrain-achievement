from fastapi import FastAPI
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
client = Anthropic()

user_goals = {}
conversation_history = []

@app.get("/")
def home():
    return {"message": "🧠 IRABrain Achievement OS", "status": "✅ Running", "version": "v1.0"}

@app.post("/set-goal")
def set_goal(goal: str):
    user_goals[goal] = {"goal": goal, "streak": 0}
    
    prompt = f"User goal: {goal}\n\nRespond as IRA coach (3 lines max): excitement + when to start + motivation"
    
    conversation_history.append({"role": "user", "content": prompt})
    
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=200,
        messages=conversation_history
    )
    
    ira_response = response.content[0].text
    conversation_history.append({"role": "assistant", "content": ira_response})
    
    return {"goal": goal, "ira_says": ira_response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)