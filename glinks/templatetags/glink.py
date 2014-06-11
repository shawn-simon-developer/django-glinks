from django import template
from django.conf import settings
from django.utils.encoding import smart_str
from django.template import TextNode, Node

from utilities import *


register = template.Library()

def parseGlinkNode(command):
	options = {}

	for op in command:
		if "=" in op:
			tmp_list = op.split("=")
			if tmp_list[0] in possibleGlinkOptions():
				options[tmp_list[0]] = tmp_list[1].replace('"', '').replace("'", '').strip()
			else:
				print glinkErrorLead() + "Incorrect command given in template.\n"
		if "as" in op:
			options["as"] = command[command.index("as")+1]
	return options

class GlinkNode(Node):
	def __init__(self, parser, token):
		command = token.split_contents()
		self.must_be_first = None
		self.as_var = None
		self.blueprint = None
		self.glink = None
		self.options = {}

		self.options = parseGlinkNode(command)

		for key, value in self.options.items():
			if key == "as":
				self.as_var = value
			elif key == "blueprint":
				self.blueprint = value
		
		# Nifty little switcharoo from string to object.
		self.blueprint = Blueprint.objects.get(name=self.blueprint)

		try:
			glinks = Glink.objects.filter(blueprint=self.blueprint)
			self.glink = glinks.order_by('?')[0]
		except Exception as e:
			print str(e)

	def render(self, context):
		return self.glink.image.url

@register.assignment_tag
def getRandomGlink():
	return Glink.objects.all().order_by('?')[0]
		
@register.tag
def glink(parser, token):
	node = GlinkNode(parser, token)
	return node


