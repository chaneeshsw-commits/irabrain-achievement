from sqlalchemy import create_engine, Column,String,DateTime
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import uuid

DATABASE_URL ="sqlite:///goals.db"  
engine =create_engine(DATABASE_URL)
sessionlocal = sessionmaker(bind=engine)
Base =declarative_base()
class Goal(Base):
      __tablename__ ="goals"
      id=Column(String,primary_key=True)
      goal = Column(String)
      streak = Column(String,default="0")
      created_at = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)
def save_goal(goal_text):
    db = sessionlocal()
    new_goal = Goal(id=goal_text, goal=goal_text)
    db.add(new_goal)
    db.commit()
    return new_goal
def get_goals():   
     db = sessionlocal()   

     return db.query(Goal).all()
def log_completion(goal_text):
    db =sessionlocal()
    goal = db.query(Goal).filter(Goal.goal == goal_text).first()
    if goal:
         goal.streak = str(int(goal.streak)+1)
         db.commit()
         return goal
    
def save_goal(goal_text):
    db = sessionlocal()
    
    # Check if goal already exists (new!)
    existing = db.query(Goal).filter(Goal.goal == goal_text).first()
    if existing:
        return existing  # Don't save again!
    
    new_goal = Goal(id=goal_text, goal=goal_text)
    db.add(new_goal)
    db.commit()
    return new_goal   
def log_missed(goal_text, reasone):
     db = sessionlocal()
     goal =db.query(Goal).filter(Goal.goal ==goal_text).first()
     if goal:
          goal.streak ="0"
          db.coomit()
          return goal
          
import uuid
from datetime import datetime

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    goal_id = Column(String)
    user_message = Column(String)
    ira_response = Column(String)
    timestamp = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)

def save_conversation(goal_id, user_msg, ira_msg):
    db = sessionlocal()
    conv = Conversation(
        id=str(uuid.uuid4()),
        goal_id=goal_id, 
        user_message=user_msg, 
        ira_response=ira_msg
    )
    db.add(conv)
    db.commit()

def get_conversation_history(goal_id):
    db = sessionlocal()
    return db.query(Conversation).filter(Conversation.goal_id == goal_id).all()    