```python
# Create Ingredients
i1 = Ingredient(name='egg')
i2 = Ingredient(name='sugar')
i3 = Ingredient(name='salt')

# Create RecipeIngredients
ri1 = RecipeIngredient(ingredient=i1, quantity=3, measurement='unit')
ri2 = RecipeIngredient(ingredient=i2, quantity=1, measurement='tb')
ri3 = RecipeIngredient(ingredient=i3, quantity=0.5, measurement='tsp')

db.session.bulk_save_objects([i1, i2, i3, ri1, ri2, ri3])
db.session.commit()

# Create Recipe
r = Recipe(name='Tamago', instructions='mix egg, salt, and sugar', minutes=10)
r.Ingredients.extend([ri1, ri2, ri3])

db.session.add(r)
db.session.commit()
```