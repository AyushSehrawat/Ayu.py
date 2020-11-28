from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

print('Welcome to Isitdown')
site = input('Way - https/http://url\n>>> ')


req = Request(site)
try:
    response = urlopen(req)
except HTTPError as err:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', err.code)
except URLError as err:
    print('We failed to reach a server.')
    print('Reason: ', err.reason)
else:
    print ('Website is working fine')