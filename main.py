#coding: utf-8
import webapp2

from controllers.HomePage import HomePageHandler
from controllers.Api import InserirClienteHandler

app = webapp2.WSGIApplication([
		('/',  HomePageHandler),
		('/api/inserirCliente',InserirClienteHandler)
], debug=True)
