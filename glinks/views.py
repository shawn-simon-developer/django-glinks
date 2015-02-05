from django.http import HttpResponse, HttpResponseRedirect
from glinks.models import Glink, Blueprint, ClickTracking
from glinks.templatetags.utilities import *

# Create your views here.
def glink_counter(request, glink_id):
	glink = Glink.objects.get(pk=glink_id)
	glink.clicks = glink.clicks + 1
	glink.save()

	ip = getClientIpFromRequest(request)
	#tracking_dict = getLocationFromIp(ip)

	clickTracking = ClickTracking(glink_id=glink, ip=ip)
	clickTracking.save()

	return HttpResponse("<meta http-equiv=\'refresh\' content=\'0; url="+glink.URL+"\'/>") if glink.URL else HttpResponse("<meta http-equiv=\'refresh\' content=\'0; url=/\'/>")
