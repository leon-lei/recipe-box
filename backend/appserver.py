"""
Creates an application instance and runs the dev server
"""

if __name__ == '__main__':  
    from recipesapi.application import create_app
    app = create_app()
    app.run()
