from django.contrib import admin
from glinks.models import Blueprint, Glink

class GlinkAdmin(admin.ModelAdmin):
	def get_readonly_fields(self, request, obj=None):
		return ['impressions', 'clicks']

# Register your models here.
admin.site.register(Blueprint)
admin.site.register(Glink, GlinkAdmin)