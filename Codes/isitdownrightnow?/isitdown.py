import urllib.request


print('Welcome to Isitdown')

site = input('URL: ')


try:
    code = urllib.request.urlopen(site).getcode()
except ValueError:
    code = 0
except urllib.error.URLError:
    code = 1 



if code == 200:
    print(f'{site} is up :)')

elif code == 0:
    print('Unknown Url type :(')

elif code == 1:
    print('Unknown address :(')

else:
    print(f'{site} is down :(')
