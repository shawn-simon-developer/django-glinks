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

class GlinkNodeCustom(Node):
	child_nodelists = ('nodelist_file', 'nodelist_empty')

	def __init__(self, parser, token):
		command = token.split_contents()
		self.must_be_first = None
		self.as_var = None
		self.blueprint = None
		self.glink = None
		self.options = {}
		self.nodelist_file = None

		self.options = parseGlinkNode(command)

		for key, value in self.options.items():
			if key == "blueprint":
				self.blueprint = value

		# Close block.
		if command[-2] == 'as':
			self.as_var = command[-1]
			self.nodelist_file = parser.parse(('empty', 'endcustom_glink',))
			if parser.next_token().contents == 'empty':
				self.nodelist_empty = parser.parse(('endcustom_glink',))
				parser.delete_first_token()
		
		# Nifty little switcharoo from string to object.
		self.blueprint = Blueprint.objects.get(name=self.blueprint)

		try:
			glinks = Glink.objects.filter(blueprint=self.blueprint)
			self.glink = glinks.order_by('?')[0]

			# Increment impression count.
			self.glink.impressions = self.glink.impressions + 1
			self.glink.save()
		except Exception as e:
			print str(e)

	def render(self, context):
		output = None

		if self.as_var:
			context.push()
			context[self.as_var] = self.glink
			output = self.nodelist_file.render(context)
			context.pop()
		else:
			output = self.glink.image.url

		return output

class GlinkNode(Node):
	child_nodelists = ('nodelist_file', 'nodelist_empty')

	def __init__(self, parser, token):
		command = token.split_contents()
		self.must_be_first = None
		self.as_var = None
		self.blueprint = None
		self.glink = None
		self.options = {}
		self.nodelist_file = None

		self.options = parseGlinkNode(command)

		for key, value in self.options.items():
			if key == "blueprint":
				self.blueprint = value
		# Nifty little switcharoo from string to object.
		self.blueprint = Blueprint.objects.get(name=self.blueprint)

		try:
			glinks = Glink.objects.filter(blueprint=self.blueprint)
			self.glink = glinks.order_by('?')[0]

			# Increment impression count.
			self.glink.impressions = self.glink.impressions + 1
			self.glink.save()
		except Exception as e:
			print str(e)

	def render(self, context):
		glink_page = "'glink/" + str(self.glink.pk) + "'"
		img_lead = "<img src="
		img_url = "'" + str(self.glink.image.url) + "'"
		on_click = " onclick=location.href="
		glink_page = "'/glink/" + str(self.glink.pk) + "'"
		img_close = ">"
 		print img_lead + img_url + on_click + glink_page + img_close
		return img_lead + img_url + on_click + glink_page + img_close


@register.assignment_tag
def getRandomGlink():
	return Glink.objects.all().order_by('?')[0]
		
@register.tag
def custom_glink(parser, token):
	node = GlinkNodeCustom(parser, token)
	return node

@register.tag
def glink(parser, token):
	node = GlinkNode(parser, token)
	return node


