from django.http import HttpResponseRedirect
from glinks.models import Glink, Blueprint, ClickTracking
from glinks.templatetags.utilities import *

# Create your views here.
def glink_counter(request, glink_id):
	glink = Glink.objects.get(pk=glink_id)
	glink.clicks = glink.clicks + 1
	glink.save()

	ip = getClientIpFromRequest(request)
	tracking_dict = getLocationFromIp(ip)

	clickTracking = ClickTracking(glink_id=glink, ip=ip, latitude=tracking_dict["Latitude"], 
				longitude=tracking_dict["Longitude"], country=tracking_dict["Country"], 
				city=tracking_dict["City"])
	clickTracking.save()

	return HttpResponseRedirect(glink.URL)