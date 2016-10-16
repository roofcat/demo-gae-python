# encoding:utf-8


from google.appengine.ext import ndb


class Contacto(ndb.Model):
    nombre = ndb.StringProperty()
    email = ndb.StringProperty()
    comentario = ndb.TextProperty()
    fecha_registro = ndb.DateTimeProperty(auto_now_add=True)

    def listar_contactos(self):
        return Contacto.query().fetch()

    def buscar_contacto(self, email):
        return Contacto.query(Contacto.email == email).get()
