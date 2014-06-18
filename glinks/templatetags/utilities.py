from glinks.models import Glink, Blueprint

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
