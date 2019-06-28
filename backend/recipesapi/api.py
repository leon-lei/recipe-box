"""
Provides the API endpoints for consuming and producing
REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Ingredient, Recipe, RecipeIngredient

api = Blueprint('api', __name__)

@api.route('/ingredients/', methods=['GET', 'POST'])
def ingredients():
    if request.method == 'GET':
        ingredients = Ingredient.query.order_by(Ingredient.name.asc())
        return jsonify({'ingredients': [i.to_dict() for i in ingredients]})
    elif request.method == 'POST':
        data = request.get_json()
        ingredient = Ingredient(name=data['name'])
        db.session.add(ingredient)
        db.session.commit()
        return jsonify(ingredient.to_dict()), 201

@api.route('/recipes/', methods=['GET', 'POST'])
def recipes():
    if request.method == 'GET':
        recipes = Recipe.query.order_by(Recipe.minutes.asc())
        return jsonify({'recipes': [r.to_dict() for r in recipes]})
    elif request.method == 'POST':
        data = request.get_json()
        # Use when data['ingredients'] is a list of ingredient names
        # ingreds = [Ingredient.query.filter_by(name=i).one() for i in data['ingredients']]
        ingreds = [Ingredient.query.filter_by(name=data['ingredients']).one()]
        recipe_ingreds = [RecipeIngredient(ingredient=i, quantity=1, measurement='tb') for i in ingreds]
        db.session.add_all(recipe_ingreds)
        db.session.flush()
        recipe = Recipe(name=data['name'],
                        Ingredients=recipe_ingreds,
                        instructions=data['instructions'],
                        minutes=data['minutes'],
                        )
        db.session.add(recipe)
        db.session.commit()
        return jsonify(recipe.to_dict()), 201

@api.route('/recipes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def recipe(id):
    if request.method == 'GET':
        recipe = Recipe.query.get_or_404(id)
        return jsonify({'recipe': recipe.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json()
        recipe = Recipe.query.get_or_404(id)
        
        recipe.name = data['name']
        recipe.ingredients = data['ingredients']
        recipe.instructions = data['instructions']
        recipe.minutes = data['minutes']
        
        db.session.commit()
        recipe = Recipe.query.get(id)
        return jsonify(recipe.to_dict()), 201
    elif request.method == 'DELETE':
        recipe = Recipe.query.get_or_404(id)
        db.session.delete(recipe)
        db.session.commit()
        return jsonify(recipe.to_dict()), 200
