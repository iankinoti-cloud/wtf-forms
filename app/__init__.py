from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import config

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app import models  # noqa: F401  (register models with SQLAlchemy)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
