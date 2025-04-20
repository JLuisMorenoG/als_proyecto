from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app import get_sirope, login_manager

bp = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    s = get_sirope()
    return Usuario.buscar_por_email(s, user_id)


@bp.route("/login", methods=["GET", "POST"])
def login():
    s = get_sirope()

    if request.method == "POST":
        email = request.form["email"]
        contrasinal = request.form["contrasinal"]

        usuario = Usuario.buscar_por_email(s, email)

        if usuario and usuario.contrasinal == contrasinal:
            login_user(usuario)
            return redirect(url_for("publicaciones.index"))
        else:
            flash("Usuario o contraseña incorrectos")

    return render_template("auth/login.html")


@bp.route("/registro", methods=["GET", "POST"])
def registro():
    s = get_sirope()

    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        contrasinal = request.form["contrasinal"]

        if Usuario.buscar_por_email(s, email):
            flash("Ese correo ya está registrado.")
            return redirect(url_for("auth.registro"))

        usuario = Usuario(nombre, email, contrasinal)
        s.save(usuario)
        login_user(usuario)
        return redirect(url_for("publicaciones.index"))

    return render_template("auth/registro.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
