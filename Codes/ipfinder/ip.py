import socket
from requests import get

print('Python alternative to find whatismyip!')
print('Author - AyushSehrawat(Github)\n\n')

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get("https://api.ipify.org").text

print(f'HOSTNAME: {hostname}')
print(f'Local IP: {local_ip}')
print(f'Public IP: {public_ip}\n')

