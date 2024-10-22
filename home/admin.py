from django.contrib import admin


from .models import UserSession

class UserSessionAdmin(admin.ModelAdmin):
	list_display = [
		'user', 'ip_address', 
		'city', 'region', 'country', 'location', 'device', 'os',
		'organisation', 'postal', 'timezone', 'created_at'
	]
admin.site.register(UserSession, UserSessionAdmin)