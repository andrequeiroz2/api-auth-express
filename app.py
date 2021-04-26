import os
from flask import Flask
from express import database
from express.database import db


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'api-express:api-auth/todo-api'
    basedir = os.path.abspath(os.path.dirname('express/database/'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db') 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    database.init_app(app)

    # blueprint for auth routes in our app
    from express.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from express.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        db.create_all()
        

    return app