from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    phone_number = Column(String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone number must have exactly ten digits.")
        return phone_number



class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content_length(self, key, content):
        if len(content) < 250:
            raise ValueError("Content must be at least 250 characters long.")
        return content
    
    @validates('summary')
    def validate_summary_length(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Summary must be a maximum of 250 characters.")
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        if category not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Category must be either Fiction or Non-Fiction.")
        return category
    
    @validates('title')
    def validate_title(self, key, title):
        keywords = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(keyword in title for keyword in keywords):
            raise ValueError("Title must contain at least one of the following: 'Won't Believe', 'Secret', 'Top [number]', 'Guess'.")
        return title


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'






''' How key can be used

    @validates('publication_year')
    def validate_publication_year(self, key, publication_year):
        if key == 'publication_year' and self.category == 'Fiction':
            # Fiction books must have a publication year before 1900
            if publication_year >= 1900:
                raise ValueError("Fiction books must have a publication year before 1900.")
        # You can add more validation logic for other categories here
        return publication_year

'''