from django import template
from django.conf import settings
from django.utils.encoding import smart_str
from django.template import TextNode, Node

from utilities import *


register = template.Library()

from random import randint

import urllib

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

		try:
			# Nifty little switcharoo from string to object.
			self.blueprint = Blueprint.objects.get(name=self.blueprint)
			glinks = Glink.objects.filter(blueprint=self.blueprint)
			if len(glinks) > 0:
				self.glink = glinks.order_by('?')[0]

				# Increment impression count.
				self.glink.impressions = self.glink.impressions + 1
				self.glink.save()
			else:
				self.glink = None
		except Exception as e:
			print str(e)
			self.glink = None

	def render(self, context):
		output = ""

		if self.glink != None:
			if self.as_var:
				context.push()
				context[self.as_var] = self.glink
				output = self.nodelist_file.render(context)
				context.pop()
			else:
				output = self.glink.image.url
		else:
			output = ""

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

		try:
			# Nifty little switcharoo from string to object.
			self.blueprint = Blueprint.objects.get(name=self.blueprint)
			glinks = Glink.objects.filter(blueprint=self.blueprint)

			if len(glinks) > 0:
				weight_list = generateWeightedListFromGlinks(glinks)

				weight = weight_list[randint(0, len(weight_list)-1)]
				glinks = glinks.filter(weight=weight)
				self.glink = glinks.order_by('?')[0]

				# Increment impression count.
				self.glink.impressions = self.glink.impressions + 1
				self.glink.save()
			else:
				self.glink = None
	
		except Exception as e:
			print str(e)
			self.glink = None

	def render(self, context):
		user_ip = get_client_ip(context['request'])
		tracking_dict = getLocationFromIp(user_ip)

		#height="42" width="42"
		'''
		glink_page = "'glink/" + str(self.glink.id) + "'"
		img_lead = "<img src="
		img_url = "'" + str(self.glink.image.url) + "'"
		on_click = " onclick=location.href="
		glink_page = "'/glink/" + str(self.glink.id) + "'"
		height = " height='" + str(self.blueprint.height) + "'"
		width = " width='" + str(self.blueprint.width) + "'"
		img_close = ">"
		return img_lead + img_url + on_click + glink_page + height + width + img_close
		'''
		if self.glink != None:
			impressionTracking = ImpressionTracking(glink_id=self.glink, latitude=tracking_dict["Latitude"], longitude=tracking_dict["Longitude"],
				country=tracking_dict["Country"], city=tracking_dict["City"])
			impressionTracking.save()

			a_lead = "<a href="
			glink_page = "'/glink/" + str(self.glink.id) + "'>"
			img_lead = "<img src="
			img_url = "'" + str(self.glink.image.url) + "'"
			height = " height='" + str(self.blueprint.height) + "'"
			width = " width='" + str(self.blueprint.width) + "'"
			img_close = "> "
			a_close = "</a>"
			return a_lead + glink_page + img_lead + img_url + height + width + img_close + a_close
		else: 
			return ""

def tracker(request):
	pass


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

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def getLocationFromIp(ip):
	address = 'http://api.hostip.info/get_html.php?ip=' + ip + '&position=true'
	location_data = urllib.urlopen(address).read()
	data_list = [s.strip() for s in location_data.splitlines()]
	data_list.remove('')
	tracking_dict = {}
	for data in data_list:
		info_list = data.split(':')
		tracking_dict[info_list[0]] = info_list[1]
	return tracking_dict






