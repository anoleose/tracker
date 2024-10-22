from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import UserSession

from .utils import (get_client_ip, get_client_city, get_client_region, 
	get_client_country, get_client_loc, get_client_org, get_client_postal, get_client_timezone, get_os, get_company_name_device
	)
from browser_history import get_history


def home(request):
	# outputs = get_history()
	# his = outputs.histories
	# list_hist = his[-5:]
	# for his in list_hist:
	# 	print(his[1:])
	user         = request.user
	ip_address   = get_client_ip(request)
	city         = get_client_city(request)
	region       = get_client_region(request)
	country      = get_client_country(request)
	location     = get_client_loc(request)
	os           = get_os(request)
	device       = get_company_name_device(request)
	organisation = get_client_org(request)
	postal       = get_client_postal(request)
	timezone     = get_client_timezone(request)

	print(user, ip_address, city, region, country, location, os, device, organisation, postal, timezone)

	if country != "unknown":
		UserSession.objects.create(
			user=user,
			ip_address=ip_address,
			city=city,
			region=region,
			country=country,
			location=location,
			os=os,
			organisation=organisation,
			postal=postal,
			timezone=timezone,
		)

	context = {}

	template = loader.get_template('home/home.html')
	return HttpResponse(template.render(context, request))


def handler404(request, exception=None):
	context = {
		'message':'SORRY PAGE DOES NOT EXIST.'
	}

	template = loader.get_template('errors/404.html')
	return HttpResponse(template.render(context, request), status=404)	



def handler500(request, exception=None):
	context = {

	}

	template = loader.get_template('errors/500.html')
	return HttpResponse(template.render(context, request), status=500)



def handler403(request, exception=None):
	context = {

	}

	template = loader.get_template('errors/403.html')
	return HttpResponse(template.render(context, request), status=403)	



def handler400(request, exception=None):
	context = {

	}

	template = loader.get_template('errors/400.html')
	return HttpResponse(template.render(context, request), status=400)	


