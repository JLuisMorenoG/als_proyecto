from datetime import datetime

class Comentario:
    def __init__(self, autor_email, contenido, publicacion_id, fecha=None):
        self.autor_email = autor_email
        self.contenido = contenido
        self.publicacion_id = publicacion_id  # Referencia a la publicación comentada
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M:%S')}] {self.autor_email}: {self.contenido}"

    @staticmethod
    def obtener_por_publicacion(sirope_instancia, publicacion_id):
        return [c for c in sirope_instancia.load_all(Comentario) if c.publicacion_id == publicacion_id]
