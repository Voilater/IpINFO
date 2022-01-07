import requests, pyfiglet

G = '\033[32m' # green

banner = pyfiglet.figlet_format("IpINFO",font="slant")

print("coded by Voilater v0.1"+G)

print(banner)

ip = "142.250.182.110"

json_url ="http://ip-api.com/json/"

data = requests.get(json_url + ip)

print(data.json())
