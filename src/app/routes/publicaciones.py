from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint("publicaciones", __name__)

@bp.route("/")
@login_required
def index():
    return render_template("publicaciones/index.html", usuario=current_user)
