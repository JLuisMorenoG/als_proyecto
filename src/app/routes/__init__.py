from . import auth, publicaciones

app.register_blueprint(auth.bp)
app.register_blueprint(publicaciones.bp)
