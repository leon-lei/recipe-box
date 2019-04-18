Recipe Box
==========================
Flask application to store cooking recipes


Future features
---------------
- Use Blueprints
- Search recipes
- Sort recipes
    - Name
    - Cooking Time

Database setup (SQLite)
---------------
```bash
# Within backend directory
# Should create recipes.db
$: python manage.py db init
$: python manage.py db migrate
$: python manage.py db upgrade
```

Start app
---------------
```bash
$: python appserver.py
```

Activate shell
---------------
```bash
$: python manage.py shell
```

Reference materials
---------------
- [Michael Herman's tutorial on testdrive.io](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/ "Michael Herman's Tutorial")

- [Adam McQuistan's tutorial on Stack Abuse](https://stackabuse.com/single-page-apps-with-vue-js-and-flask-restful-api-with-flask/ "Adam McQuistan's Tutorial")
