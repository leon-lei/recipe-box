"""
Data classes for the recipesapi application
"""

from datetime import datetime  
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    minutes = db.Column(db.Integer)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    ingredients=self.ingredients,
                    instructions=self.instructions,
                    minutes=self.minutes)
