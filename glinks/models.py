from django.db import models
from django.conf import settings


# Create your models here.
class Blueprint(models.Model):

	# Name of blueprint
	name   = models.CharField(max_length=50, null=True, blank=False)

	# Height/width in pixels
	height = models.IntegerField(null=True, blank=True)
	width  = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.name

class Glink(models.Model):

	blueprint = models.ForeignKey(Blueprint, null=True)

	# Name (Issue #2 requested.)
	name = models.CharField(null=False, blank=False, max_length=200)

	# Glink image
	image  = models.ImageField(null=False, blank=False, upload_to="glink_images")

	# Glink target URL
	URL    = models.CharField(max_length=200, null=True, blank=True)

	weight = models.PositiveIntegerField(max_length=9, default=0)

	start_date = models.DateTimeField(null=True, blank=True)
	expiry_date  = models.DateTimeField(null=True, blank=True)

	# Click/impression tracking
	clicks = models.BigIntegerField(null=False, blank=True, default=0)
	impressions = models.BigIntegerField(null=False, blank=True, default=0)

	def __unicode__(self):
		return self.name

	def mostClicksLocation(self):
		clickTracking = ClickTracking.objects.filter(glink_id=self)
		tracking_dict = {}

		for tracking in clickTracking:
			key = tracking.city + ", " + tracking.country
			tracking_dict[key] = 0

		for key in tracking_dict.keys():
			keys = key.split(",")
			tracking_at_locations = ClickTracking.objects.filter(city=keys[0], country=keys[1].strip())
			tracking_dict[key] = len(tracking_at_locations)

		sorted_tracking_dict = sorted(tracking_dict.items(), key=lambda x:x[1])

		top = ""
		if len(sorted_tracking_dict) >= 1:
			top = top + str(sorted_tracking_dict[-1][0]) + " clicked this ad " + str(sorted_tracking_dict[-1][1]) + " times."

		return top

	def mostViewedLocation(self):
		impressionTracking = ImpressionTracking.objects.filter(glink_id=self)
		tracking_dict = {}

		for tracking in impressionTracking:
			key = tracking.city + ", " + tracking.country
			tracking_dict[key] = 0

		for key in tracking_dict.keys():
			keys = key.split(",")
			tracking_at_locations = ImpressionTracking.objects.filter(city=keys[0], country=keys[1].strip())
			tracking_dict[key] = len(tracking_at_locations)

		sorted_tracking_dict = sorted(tracking_dict.items(), key=lambda x:x[1])

		top = ""
		if len(sorted_tracking_dict) >= 1:
			top = top + str(sorted_tracking_dict[-1][0]) + " viewed this ad " + str(sorted_tracking_dict[-1][1]) + " times."

		return top

	mostViewedLocation.short_description = "Most Impressions Location"
	mostViewedLocation.editable = False

	mostClicksLocation.short_description = "Most Clicks Location"
	mostClicksLocation.editable = False



class ImpressionTracking(models.Model):

	glink_id = models.ForeignKey(Glink, verbose_name="Parent Glink")

	ip = models.CharField(null=False, blank=True, max_length=100)

	latitude = models.CharField(null=False, blank=True, max_length=20)

	longitude = models.CharField(null=False, blank=True, max_length=20)

	country = models.CharField(null=False, blank=True, max_length=200)

	city = models.CharField(null=False, blank=True, max_length=200)

	def __unicode__(self):
		return "User from: " + str(self.country) + ", " + str(self.city)

class ClickTracking(models.Model):

	glink_id = models.ForeignKey(Glink, verbose_name="Parent Glink")

	ip = models.CharField(null=False, blank=True, max_length=100)

	latitude = models.CharField(null=False, blank=True, max_length=20)

	longitude = models.CharField(null=False, blank=True, max_length=20)

	country = models.CharField(null=False, blank=True, max_length=200)

	city = models.CharField(null=False, blank=True, max_length=200)

	def __unicode__(self):
		return "User from: " + str(self.country) + ", " + str(self.city)

class SpamBlockList(models.Model):

	ip = models.CharField(null=False, blank=True, max_length=100)

	



