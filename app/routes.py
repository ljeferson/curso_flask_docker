def load(app):
    from app.home import home
    from app.auth import auth
    app.register_blueprint(home)
    app.register_blueprint(auth)