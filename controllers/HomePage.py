#coding: utf-8
from models.Cliente import Cliente
import datetime
import json
from lib.Handler import Handler

class HomePageHandler(Handler):
	def get(self):
		self.render(template="index.html")
