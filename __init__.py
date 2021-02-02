from .login_manager import login_manager
from flask import Flask, Blueprint, render_template

from .models import db
from .config import DevelopmentConfig, ProductionConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    login_manager.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    return app