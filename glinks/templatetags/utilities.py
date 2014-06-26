from glinks.models import Glink, Blueprint, ImpressionTracking

import urllib


def possibleGlinkOptions():
	options = ["blueprint", "as"]
	return options

def glinkErrorLead():
	return "\nError in glinks:\n"

def generateWeightedListFromGlinks(glinks):
	weight_list = []
	for glink in glinks:
		if glink.weight not in weight_list:
			for x in range(glink.weight):
				weight_list.append(glink.weight)
	return weight_list

def getClientIpFromRequest(request):
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
		tracking_dict[info_list[0].strip()] = info_list[1].strip()
	return tracking_dict
