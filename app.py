from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager

db=SQLAlchemy()
csrf = CSRFProtect()

login_manager=LoginManager()
login_manager.login_view = "login.signup"
login_manager.login_message=""

def create_app(config_key):
    app = Flask(__name__)
    #앱의 config 설정
    app.config.from_object(config[config_key])     
    # SQLAlchemy와 앱을 연계한
    db.init_app(app) 
    # Migrate와 앱을 연계한다
    Migrate(app, db)
    csrf.init_app(app)

    login_manager.init_app(app)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud,url_prefix="/crud")
    from apps.auth import view as auth_view
    app.register_blueprint(auth_view.auth,url_prefix="/auth")
    from apps.login import views as login_view
    app.register_blueprint(login_view.login,url_prefix="/login")
    from apps.board import views as board_view
    app.register_blueprint(board_view.board,url_prefix="/board")

    return app

