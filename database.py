from sqlalchemy import create_engine, Column,String,DateTime
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker
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
    