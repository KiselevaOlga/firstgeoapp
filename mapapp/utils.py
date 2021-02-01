# Helper functions
from django.contrib.gis.geoip2 import GeoIP2


def get_location_data(ip):
    geo = GeoIP2()
    country = geo.country(ip)
    city = geo.city(ip)
    latit, longit = geo.lat_lon(ip)
    return country, city, latit, longit
