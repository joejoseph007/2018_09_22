import urllib.request
import urllib.parse
import re

#url='https://pythonprogramming.net'
#url='https://m-selig.ae.illinois.edu/ads/coord_database.html'
url='https://www.google.com/'

#values={'s':'basics','submit':'search'}

#data=urllib.parse.urlencode(values)
#data=data.encode('utf-8')
#req=urllib.request.Request(url,data)

req=urllib.request.Request(url)

resp=urllib.request.urlopen(req)
respData =resp.read()


#print(respData)


paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
    print(eachP)