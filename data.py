from urllib.request import urlopen
import json

jsondata = []


def fetchJSON():
    global jsondata
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = urlopen(url)
    jsondata = json.loads(response.read())["list"]


def getJsonFromDate(d):
    res = []
    for i in jsondata:
        if str(d) in i["dt_txt"]:
            res.append(i)
    return res
