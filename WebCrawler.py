import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
html = response.read()
print(html)