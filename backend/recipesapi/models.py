"""
Data classes for the recipesapi application
"""

from datetime import datetime  
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient = db.relationship('Ingredient', uselist=False)
    recipe = db.relationship('Recipe', uselist=False)
    quantity = db.Column(db.Float)
    measurement = db.Column(db.String(10))

    def to_dict(self):
        return dict(id=self.id,
                    name=self.ingredient.name,
                    quantity=self.quantity,
                    measurement=self.measurement)

    def __repr__(self):
        return f'<RecipeIngredient {self.quantity} {self.measurement}(s) of {self.recipe.name}'


class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    instructions = db.Column(db.Text, nullable=False)
    minutes = db.Column(db.Integer)
    Ingredients = db.relationship('RecipeIngredient')

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    ingredients=[i.to_dict() for i in self.Ingredients],
                    instructions=self.instructions,
                    minutes=self.minutes)

    def __repr__(self):
        return f'<Recipe id:{self.id} name:{self.name}>'


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name)

    def __repr__(self):
        return f'<Ingredient id:{self.id} name:{self.name}>'
