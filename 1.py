import urllib.request
import re
import os
from multiprocessing import Pool



url='https://m-selig.ae.illinois.edu/ads/'

def get(loc):
    global url
    url1=url+loc
    req=urllib.request.Request(url1)
    resp=urllib.request.urlopen(req)
    respData =resp.read()
    return respData

respData=get('coord_database.html')
paragraphs=re.findall(r'<a\s{1}href="([./A-Za-z0-9]+dat)">',str(respData))

def save(aerofoils):
    global url
    urllib.request.urlretrieve(url+aerofoils,aerofoils)

if(not os.path.isdir('coord')):
    os.makedirs('coord')
else:
    try:
        os.removedirs('coord')
        os.makedirs('coord')
    except:    
        import shutil
        shutil.rmtree('coord')
        os.makedirs('coord')	

y = Pool(100)
y.map(save,paragraphs)

