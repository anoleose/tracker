from django.db import models
from django.contrib.auth.models import User





class UserSession(models.Model):
	user          = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE) # User instance instance.id
	ip_address   = models.CharField(max_length=220, blank=True, null=True) #IP Field
	city          = models.CharField(max_length=100, blank=True, null=True) #min 50
	region        = models.CharField(max_length=100, blank=True, null=True) #min 50
	country       = models.CharField(max_length=100, blank=True, null=True) #min 50
	location      = models.CharField(max_length=100, blank=True, null=True) #min 50
	device        = models.CharField(max_length=100, blank=True, null=True) #min 50
	os            = models.CharField(max_length=100, blank=True, null=True) #min 50
	organisation  = models.CharField(max_length=100, blank=True, null=True) #min 50
	postal        = models.CharField(max_length=100, blank=True, null=True) #min 50
	timezone      = models.CharField(max_length=100, blank=True, null=True) #min 50
	created_at    = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.ip} {self.country}, {self.city}"