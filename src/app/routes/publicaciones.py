from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.publicacion import Publicacion
from app import get_sirope

bp = Blueprint("publicaciones", __name__)

@bp.route("/")
@login_required
def index():
    s = get_sirope()
    publicaciones = Publicacion.obtener_todas(s)
    publicaciones.sort(key=lambda p: p.fecha, reverse=True)
    return render_template("publicaciones/index.html", usuario=current_user, publicaciones=publicaciones)

@bp.route("/publicar", methods=["GET", "POST"])
@login_required
def publicar():
    s = get_sirope()

    if request.method == "POST":
        contenido = request.form["contenido"].strip()

        if not contenido:
            flash("El contenido no puede estar vacío.")
            return redirect(url_for("publicaciones.publicar"))

        pub = Publicacion(current_user.email, contenido)
        s.save(pub)
        flash("¡Publicación creada con éxito!")
        return redirect(url_for("publicaciones.index"))

    return render_template("publicaciones/publicar.html")

