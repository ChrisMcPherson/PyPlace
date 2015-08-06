from urllib.request import urlopen
from xml.etree import ElementTree as ET
import os.path

def getDays(xmlTree, dataSet):
    """
    Returns a list with sublists for each day of the forecast 
    """
    dayInForecast = 1
    for el in xmlTree.findall('.//time'):
        day = []
        day.append(el.attrib.get('day'))
        day.append(dayInForecast)
        dataSet.append(day)
        dayInForecast += 1
    return dataSet

def addAttribute(xmlTree, dataSet, element, attribute, fileExists):
    """
    Appends weather attributes to each day of the forecast 
    """
    if not fileExists:
        headerIndex = 1
    else:
        headerIndex = 0
    for el in xmlTree.findall('.//'+element): #find attribute value for each day
        for ix, day in enumerate(dataSet): #find correct day to append attribute
            if ix == headerIndex:
                day.append(el.attrib.get(attribute))
        headerIndex += 1
    return dataSet

path = 'C:\\Users\\Chris\\Desktop\\ForecastData.txt'
headers = ['day_in_forecast','Date','weather_description','precipitation','wind_direction','wind_speed_mps','temperature','pressure_hpa','humidity_pct','clouds_pct']
attributes = [['symbol', 'name'],['precipitation', 'value'],['windDirection', 'code'],['windSpeed', 'mps'],
              ['temperature', 'day'],['pressure', 'value'],['humidity', 'value'],['clouds', 'all']]
fileExists = False
dataSet = []

if os.path.isfile(path):
    forecastFile = open(path,'r+')
    fileExists = True
else:
    forecastFile = open(path, 'w')
    dataSet.append(headers)

weatherAPI = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Cleveland,us&mode=xml&units=imperial&cnt=10'
tree = ET.parse(urlopen(weatherAPI))

dataSet = getDays(tree, dataSet) #assign list to sub-lists containing each day of the 10 day forecast 

for i in attributes:
    dataSet = addAttribute(tree, dataSet, i[0], i[1], fileExists)

print(dataSet) #test

