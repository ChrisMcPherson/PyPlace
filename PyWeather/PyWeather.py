
from urllib.request import urlopen
from xml.etree import ElementTree as ET
import os.path

def getDays(xmlTree, fileExists):
    forecastDays = []
    if fileExists == 0:
        forecastDays.append(['Date']) #data header
    for el in xmlTree.findall('.//time'):
        day = []
        day.append(el.attrib.get('day'))
        forecastDays.append(day)
    return forecastDays

def addAttribute(xmlTree, list, element, attribute, header, fileExists):
    if fileExists == 0:
        spam = 1
        for i, head in enumerate(list): #add attribute header
            if i == 0:
                head.append(header)
    else:
        spam = 0
    for el in xmlTree.findall('.//'+element): #find attribute value for each day
        for ix, day in enumerate(list): #find correct day to append attribute
            if ix == spam:
                day.append(el.attrib.get(attribute))
        spam += 1
    return list

path = 'C:\\Users\\Chris\\Desktop\\ForecastData.txt'
fileExists = 0

if os.path.isfile(path):
    forecastFile = open(path,'r+')
    fileExists = 1
else:
    forecastFile = open(path, 'w')


weatherAPI = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Cleveland,us&mode=xml&units=imperial&cnt=10'
tree = ET.parse(urlopen(weatherAPI))

dataSet = getDays(tree, fileExists) #assign list to sub-lists containing each day of the 10 day forecast 

dataSet = addAttribute(tree, dataSet, 'symbol', 'name', 'weather_description', fileExists) #Parse through forecast attributes. Add/Remove to change data set
dataSet = addAttribute(tree, dataSet, 'precipitation', 'value', 'precipitation', fileExists) 
dataSet = addAttribute(tree, dataSet, 'windDirection', 'code', 'wind_direction', fileExists) 
dataSet = addAttribute(tree, dataSet, 'windSpeed', 'mps', 'wind_speed_mps', fileExists) 
dataSet = addAttribute(tree, dataSet, 'temperature', 'day', 'temperature', fileExists) 
dataSet = addAttribute(tree, dataSet, 'pressure', 'value', 'pressure_hpa', fileExists) 
dataSet = addAttribute(tree, dataSet, 'humidity', 'value', 'humidity_pct', fileExists) 
dataSet = addAttribute(tree, dataSet, 'clouds', 'all', 'clouds_pct', fileExists) 
print(dataSet) #test

