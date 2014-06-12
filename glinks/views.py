from django.http import HttpResponseRedirect
from glinks.models import Glink, Blueprint

# Create your views here.
def glink_counter(request, glink_id):
	glink = Glink.objects.get(pk=glink_id)
	glink.clicks = glink.clicks + 1
	glink.save()
	return HttpResponseRedirect(glink.URL)