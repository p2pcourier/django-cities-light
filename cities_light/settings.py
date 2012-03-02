import os.path

from django.conf import settings

"""
To populate cities, you should use: CITIES_LIGHT_CITY_SOURCES.
You can set it as such::

    CITIES_LIGHT_CITY_SOURCES = (
        'http://download.geonames.org/export/zip/VI.zip',
        'http://download.geonames.org/export/zip/RU.zip',
        'http://download.geonames.org/export/zip/DE.zip',
        # and so on
    )

If you want them all::

    CITIES_LIGHT_CITY_SOURCES = (
        'http://download.geonames.org/export/zip/allCountries.zip',
    )
"""

CITY_SOURCES = getattr(settings, 'CITIES_LIGHT_CITY_SOURCES', [])
COUNTRY_SOURCES = getattr(settings, 'CITIES_LIGHT_COUNTRY_SOURCES',
    ['http://download.geonames.org/export/dump/countryInfo.txt'])

ENABLE_POSTAL_CODE = getattr(settings, 'CITIES_LIGHT_ENABLE_POSTAL_CODES', False)
ENABLE_CITY = ENABLE_POSTAL_CODE or getattr(settings, 'CITIES_LIGHT_ENABLE_CITY', True)

SOURCES = list(COUNTRY_SOURCES) + list(CITY_SOURCES)

WORK_DIR = getattr(settings, 'CITIES_LIGHT_WORK_DIR',
    os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'var')))