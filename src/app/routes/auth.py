from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app import get_sirope, login_manager

bp = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    s = get_sirope()
    return Usuario.buscar_por_email(s, user_id)
