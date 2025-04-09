from flask import Flask
from flask_login import LoginManager
import sirope

login_manager = LoginManager()
s = None

def create_app():
    global s
    app = Flask(__name__)
    app.secret_key = 'tu-clave-secreta'  # cámbiala por seguridad

    s = sirope.Sirope()

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # ruta donde redirigir si no logueado

    from .routes import auth, publicaciones

    app.register_blueprint(auth.bp)
    app.register_blueprint(publicaciones.bp)

    return app

def get_sirope():
    global s
    return s
