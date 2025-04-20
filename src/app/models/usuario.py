import sirope
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, nombre, email, contrasinal):
        self.nombre = nombre
        self.email = email
        self.contrasinal = contrasinal  

    def __str__(self):
        return f"{self.nombre} <{self.email}>"

    def get_id(self):
        """Método obligatorio para Flask-Login"""
        return self.email

    @staticmethod
    def buscar_por_email(sirope_instancia, email):
        usuarios = sirope_instancia.load_all(Usuario)
        for u in usuarios:
            if u.email == email:
                return u
        return None
