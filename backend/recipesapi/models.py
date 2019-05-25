"""
Data classes for the recipesapi application
"""

from datetime import datetime  
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

ingredients = db.Table('ingredients',
    db.Column('ingr_id', db.Integer, db.ForeignKey('ingredient.ingr_id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.recipe_id'), primary_key=True)
)


class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    instructions = db.Column(db.Text, nullable=False)
    minutes = db.Column(db.Integer)

    ingredients = db.relationship('Ingredient', secondary=ingredients, lazy='subquery',
                backref=db.backref('recipes', lazy=True))

    def to_dict(self):
        return dict(recipe_id=self.recipe_id,
                    name=self.name,
                    ingredients=self.ingredients,
                    instructions=self.instructions,
                    minutes=self.minutes)

    def __repr__(self):
        return f'<Recipe recipe_id:{recipe_id} recipe_name:{name}>'


class Ingredient(db.Model):
    ingr_id = db.Column(db.Integer, primary_key=True)
    ingr_name = db.Column(db.String(120), nullable=False, unique=True)

    def to_dict(self):
        return dict(ingr_id=self.ingr_id,
                    ingr_name=self.ingr_name)

    def __repr__(self):
        return f'<Ingredient ingr_id:{ingr_id} ingr_name:{ingr_name}>'
