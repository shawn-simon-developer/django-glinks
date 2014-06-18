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

	# Glink image
	image  = models.ImageField(null=False, blank=False, upload_to="glink_images")

	# Glink target URL
	URL    = models.URLField(null=True, blank=True)

	weight = models.PositiveIntegerField(max_length=9, default=0)

	# Click/impression tracking
	clicks = models.BigIntegerField(null=False, blank=True, default=0)
	impressions = models.BigIntegerField(null=False, blank=True, default=0)