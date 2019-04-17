from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Recipe Class/Model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    minutes = db.Column(db.Integer)

    def __init__(self, name, ingredients, instructions, minutes):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.minutes = minutes

    def __repr__(self):
        return f'Recipe({self.name} - {self.minutes} minutes)'

# Recipe Schema
class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'ingredients', 'instructions', 'minutes')

# Init schema
recipe_schema = RecipeSchema(strict=True)
recipes_schema = RecipeSchema(many=True, strict=True)


@app.route('/', methods=['GET'])
def homepage():
    all_recipes = Recipe.query.order_by(Recipe.name.asc())
    result = recipes_schema.dump(all_recipes)
    return jsonify(result.data)

@app.route('/recipe/new', methods=['POST'])
def new_recipe():
    name = request.json['name']
    ingredients = request.json['ingredients']
    instructions = request.json['instructions']
    minutes = request.json['minutes']

    new_recipe = Recipe(name, ingredients, instructions, minutes)
    db.session.add(new_recipe)
    db.session.commit()
    return recipe_schema.jsonify(new_recipe)

@app.route('/recipe/<int:id>/delete', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    return recipe_schema.jsonify(recipe)


@app.route('/recipe/<int:id>/update', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get_or_404(id)

    name = request.json['name']
    ingredients = request.json['ingredients']
    instructions = request.json['instructions']
    minutes = request.json['minutes']

    recipe.name = name
    recipe.ingredients = ingredients
    recipe.instructions = instructions
    recipe.minutes = minutes

    db.session.commit()
    return recipe_schema.jsonify(recipe)


@app.route("/recipe/<int:id>")
def recipe(id):
    recipe = Recipe.query.get_or_404(id)
    return recipe_schema.jsonify(recipe)


if __name__ == '__main__':
    app.run(debug=True)
