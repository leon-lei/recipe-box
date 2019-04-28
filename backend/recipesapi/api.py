"""
Provides the API endpoints for consuming and producing
REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Recipe

api = Blueprint('api', __name__)

@api.route('/recipes/', methods=['GET', 'POST'])
def recipes():
    if request.method == 'GET':
        recipes = Recipe.query.order_by(Recipe.minutes.asc())
        return jsonify({'recipes': [r.to_dict() for r in recipes]})
    elif request.method == 'POST':
        data = request.get_json()
        recipe = Recipe(name=data['name'],
                        ingredients=data['ingredients'],
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
