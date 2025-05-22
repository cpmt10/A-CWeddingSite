from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from dotenv import load_dotenv
import os

db = SQLAlchemy()


def create_app():
    """
    This is the starting method of the flask application. All the flask BASIC configurations are done here
    """
    load_dotenv()
    app = Flask(__name__)

    # !!! WARNING: This code will not run until .env is placed in root folder with the Secret Key inside !!!
    app.secret_key = os.getenv("SECRET_KEY", "fallback-insecure-dev-key")
    app.config.from_object(Config)

    # Ensures Data Folder is created before creating the database
    os.makedirs(os.path.dirname(Config.DB_PATH), exist_ok=True)

    # Links app to SQLAlchemy
    db.init_app(app)

    # Checks if there are any new tables for database. If not it does nothing
    with app.app_context():
        from website.models.db_tables import HeadParty
        from website.services.sample_loader import load_sample_data

        db.create_all()

        # Loads the sample data
        if HeadParty.query.first() is None:
            sample_json_path = os.path.join(
                os.path.dirname(__file__), "data", "sample.json"
            )
            load_sample_data(sample_json_path)

    # Imports the views file and registers the routes inside the application
    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
