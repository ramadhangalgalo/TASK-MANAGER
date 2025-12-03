from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base, get_db

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
    
    @property
    def task_count(self):
        return len(self.tasks)
    
    @classmethod
    def create(cls, name, description, user_id):
        if not name:
            raise ValueError("Project name is required")
        
        db = get_db()
        project = cls(name=name, description=description, user_id=user_id)
        db.add(project)
        db.commit()
        db.refresh(project)
        db.close()
        return project
    
    @classmethod
    def get_all(cls):
        db = get_db()
        projects = db.query(cls).all()
        db.close()
        return projects
    
    @classmethod
    def find_by_id(cls, project_id):
        db = get_db()
        project = db.query(cls).filter(cls.id == project_id).first()
        db.close()
        return project
    
    def delete(self):
        db = get_db()
        db.delete(self)
        db.commit()
        db.close()