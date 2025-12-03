from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base, get_db

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    projects = relationship("Project", back_populates="owner", cascade="all, delete-orphan")
    
    @property
    def project_count(self):
        return len(self.projects)
    
    @classmethod
    def create(cls, name, email):
        if not name or not email:
            raise ValueError("Name and email are required")
        if "@" not in email:
            raise ValueError("Invalid email format")
        
        db = get_db()
        user = cls(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()
        return user
    
    @classmethod
    def get_all(cls):
        db = get_db()
        users = db.query(cls).all()
        db.close()
        return users
    
    @classmethod
    def find_by_id(cls, user_id):
        db = get_db()
        user = db.query(cls).filter(cls.id == user_id).first()
        db.close()
        return user
    
    def delete(self):
        db = get_db()
        db.delete(self)
        db.commit()
        db.close()