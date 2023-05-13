from flask import Flask, request, jsonify, make_response, session, abort, redirect, url_for 
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS,cross_origin

db = SQLAlchemy()
load_dotenv('.env')
def create_app():
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}'
    app.secret_key = 'd378c67c9c532726b96802eed6ced21389ab414b4eb69c9b'
    db.initialize(app)
    Migrate(app,db)
    def register_models(app):
        with app.app_context():
            db.create_all()
    def register_extensions(app):
        db
    register_extensions(app)
    register_models(app)
    return app
app = create_app()


from sqlalchemy import Column, String, Integer, ForeignKey,Text,Enum,ARRAY,Boolean , LargeBinary , PickleType

class User(db.Base_model):
    __tablename__ = "users"
    
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True, unique=True)
    password = Column(String(500), nullable=True)
    mobile=Column(String(10))
    provider = Column(String(50), nullable=True)
    iss = Column(String(100), nullable=True)
    # Role = Column(Enum('Admin', 'User','Superuser'))
    Role = Column(Enum('Admin', 'User', 'Superuser', name='role_type'))
    otp = Column(Integer(), nullable=True)
    profile_image = Column(String(100), nullable=True)
    is_active = Column(Boolean(), default=True)
  
