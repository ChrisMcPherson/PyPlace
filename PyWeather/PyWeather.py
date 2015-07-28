from urllib.request import urlopen
from xml.etree import ElementTree as ET


def getDays(xmlTree):
    forecastDays = []
    forecastDays.append(['Date']) #data header
    for el in xmlTree.findall('.//time'):
        day = []
        day.append(el.attrib.get('day'))
        forecastDays.append(day)
    return forecastDays

def addAttribute(xmlTree, list, element, attribute, header):
    for i, head in enumerate(list): #add attribute header
        if i == 0:
            head.append(header)
    spam = 1
    for el in xmlTree.findall('.//'+element): #find attribute value for each day
        for ix, day in enumerate(list): #find correct day to append attribute
            if ix == spam:
                day.append(el.attrib.get(attribute))
        spam += 1
    return list


tenDayWeather = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Cleveland,us&mode=xml&units=imperial&cnt=10'
tree = ET.parse(urlopen(tenDayWeather))

dataSet = getDays(tree) #assign list to sub-lists containing each day of the 10 day forecast 

dataSet = addAttribute(tree, dataSet, 'symbol', 'name', 'weather_description') 
dataSet = addAttribute(tree, dataSet, 'precipitation', 'value', 'precipitation') 
dataSet = addAttribute(tree, dataSet, 'windDirection', 'code', 'wind_direction') 
dataSet = addAttribute(tree, dataSet, 'windSpeed', 'mps', 'wind_speed_mps') 
dataSet = addAttribute(tree, dataSet, 'temperature', 'day', 'temperature') 
dataSet = addAttribute(tree, dataSet, 'pressure', 'value', 'pressure_hpa') 
dataSet = addAttribute(tree, dataSet, 'humidity', 'value', 'humidity_pct') 
dataSet = addAttribute(tree, dataSet, 'clouds', 'all', 'clouds_pct') 
print(dataSet) #test

