from urllib.request import urlopen
from xml.etree import ElementTree as ET


def getAttribute(xmlTree, attribute):
    for el in xmlTree.findall('.//time'):
        print(el.attrib.get(attribute))


tenDayWeather = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Cleveland,us&mode=xml&units=imperial&cnt=10'
tree = ET.parse(urlopen(tenDayWeather))
getAttribute(tree, 'day')



