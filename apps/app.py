from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db=SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    #앱의 config 설정
    app.config.from_mapping(
            SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ",
            SQLALCHEMY_DATABASE_URI =f"sqlite:///{Path(__file__).parent.parent/'local.sqlite'}", 
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLAlCHEMY_ECHO=True,
            WTF_CSRF_SECRET_KEY='AuwzyszU5sugKN7Ks6f'
            )     
    # SQLAlchemy와 앱을 연계한
    db.init_app(app) 
    # Migrate와 앱을 연계한다
    Migrate(app, db)
    csrf.init_app(app)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud,url_prefix="/crud")

    return app
