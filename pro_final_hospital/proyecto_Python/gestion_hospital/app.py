from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.setting import Config
from modelo.entidades import paciente, medico, turno
from route.paciente_route import paciente_bp
from route.medico_route import medico_bp
from route.turno_route import turno_bp

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(paciente_bp, url_prefix='/api')
    app.register_blueprint(medico_bp, url_prefix='/api')
    app.register_blueprint(turno_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
