from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from datetime import datetime

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

#semantic momory  
# database.py - Add User class


class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    total_goals = Column(Integer, default=0)
    total_completed = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    success_rate = Column(String, default="0%")

Base.metadata.create_all(engine)

def get_or_create_user():
    db = sessionlocal()
    user = db.query(User).first()
    if not user:
        user = User(id=str(uuid.uuid4()))
        db.add(user)
        db.commit()
    return user

def update_user_stats(total_goals, completed, streak):
    db = sessionlocal()
    user = db.query(User).first()
    if user:
        user.total_goals = total_goals
        user.total_completed = completed
        user.current_streak = streak
        rate = int((completed / total_goals) * 100) if total_goals > 0 else 0
        user.success_rate = f"{rate}%"
        db.commit()
# database.py

class UserPreference(Base):
    __tablename__ = "preferences"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    motivation_style = Column(String, default="gentle")  # harsh or gentle
    preferred_time = Column(String, default="morning")   # morning or evening

Base.metadata.create_all(engine)

def save_preference(motivation_style, preferred_time):
    db = sessionlocal()
    pref = UserPreference(
        id=str(uuid.uuid4()),
        motivation_style=motivation_style,
        preferred_time=preferred_time
    )
    db.add(pref)
    db.commit()        