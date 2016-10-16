# encoding:utf-8


import webapp2


import config
from models import Contacto


class HomeController(webapp2.RequestHandler):

    def get(self):
        template = config.JINJA_ENV.get_template('index.html')
        self.response.write(template.render())


class ContactoController(webapp2.RequestHandler):

    def get(self):
        template = config.JINJA_ENV.get_template('contacto/form.html')
        self.response.write(template.render())

    def post(self):
        # recibiendo parametros
        nombre = self.request.get('nombre')
        email = self.request.get('email')
        comentario = self.request.get('comentario')
        # se instancia el modelo contacto
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.email = email
        contacto.comentario = comentario
        contacto.put()
        # preparando el listado de contactos
        context = {
            'contactos': contacto.listar_contactos()
        }
        template = config.JINJA_ENV.get_template('contacto/listado.html')
        self.response.write(template.render(context))


app = webapp2.WSGIApplication([
    ('/', HomeController),
    ('/contactos', ContactoController),
], debug=True)
