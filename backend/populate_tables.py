from recipesapi.models import db, Ingredient, Recipe, RecipeIngredient
from recipesapi.application import create_app

app = create_app()

def populate():
    with app.app_context():
        i1 = Ingredient(name='egg')
        i2 = Ingredient(name='sugar')
        i3 = Ingredient(name='salt')
        db.session.add_all([i1, i2, i3])
        db.session.flush()

        ri1 = RecipeIngredient(ingredient=i1, quantity=3, measurement='unit')
        ri2 = RecipeIngredient(ingredient=i2, quantity=1, measurement='tb')
        ri3 = RecipeIngredient(ingredient=i3, quantity=0.5, measurement='tsp')
        db.session.add_all([ri1, ri2, ri3])
        db.session.flush()

        r = Recipe(name='tamago', instructions='mix egg, salt, and sugar', minutes=10)
        r.Ingredients.extend([ri1, ri2, ri3])

        db.session.add(r)
        db.session.commit()

populate()