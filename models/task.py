from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base, get_db

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    priority = Column(String, default="medium")
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    
    project = relationship("Project", back_populates="tasks")
    
    @property
    def status(self):
        return "Completed" if self.completed else "Pending"
    
    @classmethod
    def create(cls, title, description, priority, project_id):
        if not title:
            raise ValueError("Task title is required")
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be low, medium, or high")
        
        db = get_db()
        task = cls(title=title, description=description, priority=priority, project_id=project_id)
        db.add(task)
        db.commit()
        db.refresh(task)
        db.close()
        return task
    
    @classmethod
    def get_all(cls):
        db = get_db()
        tasks = db.query(cls).all()
        db.close()
        return tasks
    
    @classmethod
    def find_by_id(cls, task_id):
        db = get_db()
        task = db.query(cls).filter(cls.id == task_id).first()
        db.close()
        return task
    
    def delete(self):
        db = get_db()
        db.delete(self)
        db.commit()
        db.close()
    
    def mark_complete(self):
        db = get_db()
        self.completed = True
        db.commit()
        db.close() 