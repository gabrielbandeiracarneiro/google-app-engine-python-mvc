#coding: utf-8
from models.Cliente import Cliente
import datetime
import json
from lib.Handler import Handler
from models.Cliente import Cliente
import webapp2
from google.appengine.ext import db

class InserirClienteHandler(Handler):
	def post(self):
		try:
			query = db.GqlQuery("SELECT * FROM Cliente where cpf_cnpj = :cpf_cnpj",cpf_cnpj=self.request.get("cpf_cnpj"))
			for json in query:
				self.write_json(400,{'status':False,'exception':'Cliente já cadastrado!'})
				return
			cliente = Cliente(
				nome=self.request.get("nome"),
				cpf_cnpj=self.request.get("cpf_cnpj"),
				data_nascimento=datetime.datetime.strptime(self.request.get("data_nascimento"),"%d/%m/%Y").date(),
				idioma=self.request.get("idioma"),
				data_cadastro=datetime.datetime.today(),
				inscricao_estadual=self.request.get("inscricao_estadual"),
				status=1
			).put()
			if(cliente):
				self.write_json(200,{'status':True,'id':str(cliente)})
			else:
				self.write_json(400,{'status':False,'exception':""})
		except Exception, e:
			self.write_json(400,{'status':False,'exception':str(e)})
