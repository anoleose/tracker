from uuid import getnode as get_mac
from mac_vendor_lookup import MacLookup
from django.contrib.gis.geoip2 import GeoIP2
import requests
import json 
import platform 
import os

g = GeoIP2()
#{'country_code': 'RU', 'country_name': 'Russia'} 
#{'city': 'Orenburg', 'continent_code': 'EU', 'continent_name': 'Europe', 'country_code': 'RU', 'country_name': 'Russia', 'dma_code': None, 'is_in_european_union': False, 'latitude': 51.7898, 'longitude': 55.0984, 'postal_code': '460001', 'region': 'ORE', 'time_zone': 'Asia/Yekaterinburg'} (51.7898, 55.0984)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", None)
    return ip




def get_client_city(request):
    try:
        ip   = get_client_ip(request) 
        city = g.city(ip)
        return city 
    except:
        return "unknown"


def get_client_region(request):
    try:
        ip     = get_client_ip(request) 
        region = g.city(ip)['region']
        return region 
    except:
        return "unknown"

def get_client_country(request):
    try:
        ip     = get_client_ip(request) 
        region = g.country_name(ip)
        return region 
    except:
        return "unknown"

def get_client_loc(request):
    try:
        ip   = get_client_ip(request) 
        latitude  = g.city(ip)['latitude']
        longitude = g.city(ip)['longitude']
        return latitude, longitude
    except:
        return "unknown"


def get_client_org(request):
    try:
       ip   = get_client_ip(request)
       return "unknown"
    except:
        return "unknown"


def get_client_postal(request):
    try:
        ip   = get_client_ip(request) 
        postal_code  = g.city(ip)['postal_code']
        return postal_code
    except:
        return "unknown"

def get_client_timezone(request):
    try:
        ip   = get_client_ip(request) 
        time_zone  = g.city(ip)['time_zone']
        return time_zone
    except:
        return "unknown"

def get_os(request):
    get_browser_os = request.headers['User-Agent']
    return get_browser_os

    #system  = platform.system()
    #release = platform.release()
    #return system, release

def get_company_name_device(request):
    mac = get_mac()
    #m = ":".join(f"{b:02x}" for b in mac.to_bytes(6))
    mac_address = ":".join(f"{b:02x}" for b in mac.to_bytes(6))
    vendor_name = MacLookup().lookup(mac_address)
    return vendor_name

    