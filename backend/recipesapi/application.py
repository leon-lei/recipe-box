"""
Creates a Flask app instance and registers the database object
"""

from flask import Flask

def create_app(app_name='RECIPES_API'):
    app = Flask(app_name)
    app.config.from_object('recipesapi.config.BaseConfig')

    from recipesapi.api import api
    app.register_blueprint(api, url_prefix="/api")   

    from recipesapi.models import db
    db.init_app(app)
    
    return app