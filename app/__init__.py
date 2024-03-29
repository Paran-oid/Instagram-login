from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__,static_folder="static",template_folder="templates")
app.config.from_object(Config)
db=SQLAlchemy(app)
Migrate(app, db)

from app import routes, models