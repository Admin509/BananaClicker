import time
import mouse
from colorama import Fore
import random

click = random.randint(10,20)
delay = float(input(Fore.YELLOW + "Введите количество секунд, как задержку для цикла: "))
rdelay = 0.1

def clk():
    for _ in range(click):
        mouse.double_click()
        time.sleep(delay)

for i in range(5):
    clk()
    time.sleep()
