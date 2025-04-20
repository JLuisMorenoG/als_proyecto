from flask import Flask
from flask_login import LoginManager
import sirope

login_manager = LoginManager()
s = None  # instancia global de Sirope


def create_app():
    global s
    app = Flask(__name__)
    app.secret_key = 'clave-secreta-supersegura'  # ¡Cámbiala en producción!

    import redis
    s = sirope.Sirope(redis.Redis(host="redis", port=6379, db=0))

    # Configurar Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Registrar blueprints
    from .routes import auth, publicaciones
    app.register_blueprint(auth.bp)
    app.register_blueprint(publicaciones.bp)

    return app


def get_sirope():
    global s
    return s
