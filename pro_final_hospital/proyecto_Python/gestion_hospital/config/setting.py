import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://tu_usuario:tu_contraseña@localhost/hospital_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
