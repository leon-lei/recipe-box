Recipe Box
==========================
Application to store cooking recipes
- Backend: Flask
- Frontend: Vue

Current features
---------------
- CRUD operations for Recipes

Future features
---------------
- WYSIWYG editor to write "instructions"
- Sort recipes
    - Name
    - Cooking Time
- Negative search filter
    - No peanuts in recipe ingredients
- Image field 

Database setup (SQLite)
---------------
```bash
# Run in backend directory, should create recipes.db
# If db already exists, remove migrations directory before commands
$: python manage.py db init
$: python manage.py db migrate
$: python manage.py db upgrade
```

Start app
---------------
```bash
# backend
$: python appserver.py

# frontend
$: npm run dev
```

Activate database shell
---------------
```bash
$: python manage.py shell
```

Reference materials
---------------
- [Michael Herman's tutorial on testdriven.io](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/ "Michael Herman's Tutorial")

- [Adam McQuistan's tutorial on Stack Abuse](https://stackabuse.com/single-page-apps-with-vue-js-and-flask-restful-api-with-flask/ "Adam McQuistan's Tutorial")
