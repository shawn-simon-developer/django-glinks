from django.contrib import admin
from glinks.models import Blueprint, Glink, ImpressionTracking, ClickTracking

class GlinkAdmin(admin.ModelAdmin):
	def get_readonly_fields(self, request, obj=None):
		return ['impressions', 'clicks']

class TrackingAdmin(admin.ModelAdmin):
	def get_readonly_fields(self, request, obj=None):
		return ['glink_id', 'latitude', 'longitude', 'country', 'city']

# Register your models here.
admin.site.register(Blueprint)
admin.site.register(Glink, GlinkAdmin)
admin.site.register(ImpressionTracking, TrackingAdmin)
admin.site.register(ClickTracking, TrackingAdmin)