from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings
import requests

def lon_lat(ip):
    g = GeoIP2(path=settings.GEOIP_DIR)
    return g.coords(ip) #Returns a coordinate tuple of (longitude, latitude).

