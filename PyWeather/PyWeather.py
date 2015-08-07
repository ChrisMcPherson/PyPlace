from urllib.request import urlopen
from xml.etree import ElementTree as ET
import os.path
import csv


def getDays(xmlTree, dataSet):
    """
    Returns a master list with sublists for each day of the forecast 
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
    attributeNotEmpty = '';
    if not fileExists:
        headerIndex = 1
    else:
        headerIndex = 0
    for el in xmlTree.findall('.//'+element): #find attribute value for each day
        for ix, day in enumerate(dataSet): #find correct day to append attribute
            if ix == headerIndex:
                if not el.attrib.get(attribute):
                    attributeNotEmpty = None
                else:
                    attributeNotEmpty = el.attrib.get(attribute)
                day.append(attributeNotEmpty)
        headerIndex += 1
    return dataSet


weatherAPI = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Cleveland,us&mode=xml&units=imperial&cnt=10'
path = 'C:\\Users\\Chris\\Desktop\\ForecastData.csv'
headers = ['Date','day_in_forecast','weather_description','precipitation','wind_direction','wind_speed_mps','temperature','pressure_hpa','humidity_pct','clouds_pct']
attributes = [['symbol', 'name'],['precipitation', 'value'],['windDirection', 'code'],['windSpeed', 'mps'],
              ['temperature', 'day'],['pressure', 'value'],['humidity', 'value'],['clouds', 'all']]
fileExists = False
dataSet = []

if os.path.isfile(path):
    fileExists = True
else:
    forecastFile = open(path, 'w')
    dataSet.append(headers)

tree = ET.parse(urlopen(weatherAPI)) #Get XML tree from API

dataSet = getDays(tree, dataSet) #assign list to sub-lists containing each day of the 10 day forecast 

for i in attributes:    
    dataSet = addAttribute(tree, dataSet, i[0], i[1], fileExists)   #loop through each attribute

print(dataSet) #test

with open(path, 'a', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for row in dataSet:
        wr.writerow(row)

    

