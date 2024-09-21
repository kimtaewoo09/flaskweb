from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from apps.config import config

db=SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_key):
    app = Flask(__name__)
    #앱의 config 설정
    app.config.from_object(config[config_key])     
    # SQLAlchemy와 앱을 연계한
    db.init_app(app) 
    # Migrate와 앱을 연계한다
    Migrate(app, db)
    csrf.init_app(app)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud,url_prefix="/crud")
    from apps.auth import view as auth_view
    app.register_blueprint(auth_view.auth,url_prefix="/auth")
    return app
