from django.contrib import admin
from glinks.models import Blueprint, Glink, ImpressionTracking, ClickTracking

class GlinkAdmin(admin.ModelAdmin):
	fields = ['blueprint', 'name', 'isActive', 'weight', 'URL', 'image', 'start_date', 'expiry_date', 'impressions', 'clicks', 'mostClicksLocation', 'mostViewedLocation']

	def get_readonly_fields(self, request, obj=None):
		return ['impressions', 'clicks', 'mostClicksLocation', 'mostViewedLocation']

class ClickTrackingAdmin(admin.ModelAdmin):
	def get_readonly_fields(self, request, obj=None):
		return ['glink_id', 'latitude', 'longitude', 'country', 'city']


# Register your models here.
admin.site.register(Blueprint)
admin.site.register(Glink, GlinkAdmin)
admin.site.register(ImpressionTracking)
admin.site.register(ClickTracking, ClickTrackingAdmin)