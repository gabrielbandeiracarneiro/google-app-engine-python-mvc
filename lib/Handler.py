#coding: utf-8
import webapp2
import jinja2
import os
import json

template_dir = os.path.join(os.path.dirname(__file__),'../views')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
										autoescape = True)

def datetimeformat(value, format='%d/%m/%Y'):
	if(value):
		return value.strftime(format)
	return ""
jinja_env.filters['datetimeformat'] = datetimeformat

class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)

	def write_json(self,status,*a,**kw):
		self.response.status = status
		self.response.out.write(json.dumps(*a),**kw)

	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)

	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))