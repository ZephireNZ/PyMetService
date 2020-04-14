import requests
import re

DEFAULT_BASE = 'http://metservice.com/publicData'

TOWN_SLUG_REGEX = re.compile(r'\/([\w-]+)$')

def _get_data(endpoint: str, base: str):
    try:
        resp = requests.get(base + endpoint)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError:
        # TODO: error handling?
        return None

def _city_data(city: str, endpoint: str, base: str):
    return _get_data(endpoint.format(city), base)

def get_cities_list(base = DEFAULT_BASE):
    resp = _get_data("/webdata/towns-cities", base)

    search = resp["layout"]["search"]

    towns = {}
    for island in search:
        for region in island["items"]:
            for town in region["children"]:
                town_url = town["url"]


                towns[town["label"]] = TOWN_SLUG_REGEX.search(town_url).group(1)

    return towns

def getLocalForecast(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/localForecast{city}', base)

def getSunProtectionAlert(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/sunProtectionAlert{city}', base)

def getOneMinObs(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/oneMinObs_{city}', base)

def getHourlyObsAndForecast(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/hourlyObsAndForecast_{city}', base)

def getLocalObs(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/localObs_{city}', base)

def getTides(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/tides_{city}', base)

def getWarnings(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/warningsForRegion3_urban.{city}', base)

def getRises(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/riseSet_{city}', base)

def getPollen(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/pollen_town_{city}', base)

def getDaily(city: str, base: str = DEFAULT_BASE):
    return _get_data(f'/climateDataDailyTown_{city}_32', base)