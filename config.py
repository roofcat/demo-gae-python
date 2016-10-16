# encoding:utf-8


import os
import jinja2


JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.abspath('templates')),
    autoescape=True,
    extensions=['jinja2.ext.autoescape']
)
