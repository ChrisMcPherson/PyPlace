from urllib import Request, urlopen, URLError

request = Request('http://www.placekittens.com/')
try:
    response = urlopen(request)
    kittens = response.read()
    print(kittens[559:1000])
except URLError as e:
    print('no kittens because error', e)
