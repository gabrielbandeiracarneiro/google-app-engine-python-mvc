#coding: utf-8
import webapp2
from google.appengine.ext import db
from google.appengine.ext import ndb

class Cliente(db.Model):
	nome = db.StringProperty(indexed=True,required=True)
	data_nascimento = db.DateProperty(required=True)
	data_cadastro = db.DateTimeProperty()
	cpf_cnpj = db.StringProperty(required=True)
	status = db.IntegerProperty(indexed=True,required=True)
	inscricao_estadual = db.StringProperty()
	idioma = db.StringProperty(required=True)
