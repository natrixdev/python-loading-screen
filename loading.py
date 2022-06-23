import os 
from pystyle import Colorate, Colors
import time 
print(Colorate.Horizontal(Colors.green_to_red, "Loading Screen Python By natrix"))
print(Colorate.Horizontal(Colors.blue_to_red, "                     Github: @natrixdev"))
time.sleep(3);os.system('cls')
while True: 
    print(Colorate.Horizontal(Colors.green_to_red,"[|]")); time.sleep(0.5); os.system('cls')
    print(Colorate.Horizontal(Colors.blue_to_red,"[\]")); time.sleep(0.5); os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red,"[-]")); time.sleep(0.5); os.system('cls')
    print(Colorate.Horizontal(Colors.green_to_white,"[/]")); time.sleep(0.5); os.system('cls')
