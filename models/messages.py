from datetime import datetime
from .database import db



class Message(db.Model):
    
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    message = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default= datetime.utcnow)
    
    # mainly used for debugging and logging because it provides a readable description of an object
    def __repr__(self):
        return f'<Message {self.id}: {self.name}>'
    
    @classmethod
    def create_message(cls, name, email, message):
        # Create and save a new messae to the database
        
        new_message = cls(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        return new_message
    
    @classmethod
    def get_all_messages(cls):
        # Retrieve all messages from the database
        return cls.query.order_by(cls.created_at.desc()).all()