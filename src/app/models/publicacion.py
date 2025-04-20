from datetime import datetime

class Publicacion:
    def __init__(self, autor_email, contenido, fecha=None):
        self.autor_email = autor_email
        self.contenido = contenido
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M:%S')}] {self.autor_email}: {self.contenido}"

    @staticmethod
    def obtener_todas(sirope_instancia):
        return list(sirope_instancia.load_all(Publicacion))
