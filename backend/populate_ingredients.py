from recipesapi.models import db, Ingredient
from recipesapi.application import create_app

app = create_app()

def populate():
    with app.app_context():
        i1 = Ingredient(name='egg')
        i2 = Ingredient(name='sugar')
        i3 = Ingredient(name='salt')

        db.session.bulk_save_objects([i1, i2, i3])
        db.session.commit()

populate()