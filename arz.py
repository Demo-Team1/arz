import requests
import json
import time
from colorama import Fore,init
init()

http = requests.get("http://get-link.ir:8000/api/v2/crypto/").text
print(Fore.RED+""" 
  ████╗ ███████╗███╗   ███╗ ██████╗ ████████╗███████╗ █████╗ ███╗   ███╗
██╔══██╗██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██║  ██║█████╗  ██╔████╔██║██║   ██║   ██║   █████╗  ███████║██╔████╔██║
██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
\n""")
time.sleep(0.5)
print(Fore.BLUE+"Coded By >> : @Demo_Team >> \n@x_darkpy_x  <¤> @MrDemoam")
time.sleep(1)
myjson = json.loads(http)
for data in myjson['data']:
	print(Fore.RED+"\n*****************************************\n")
	print(Fore.GREEN+"Name"+Fore.BLUE+" : >> "+Fore.WHITE+data['name'])
	print(Fore.GREEN+"Dollar Price"+Fore.BLUE+" : >> "+Fore.WHITE+data['dollar_price'])
	print(Fore.GREEN+"Toman Price"+Fore.BLUE+" : >> "+Fore.WHITE+data['toman_price'])
	print(Fore.GREEN+"Daily Change"+Fore.BLUE+" : >> "+Fore.WHITE+data['daily_change'])
	print(Fore.GREEN+"Weekly Change"+Fore.BLUE+" : >> "+Fore.WHITE+data['weekly_change'])
#Coded by >> : Sepehr_Dark