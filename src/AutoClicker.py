#AutoClicker

import pyautogui as pg
import keyboard as key
from time import sleep


print('# ')
print('#  PythonAutoClicker')
print('# ')
print('# f6 - on&off script')
print('# f3 - end script')

activated = False

def clicker():
    pg.click(pg.position())

while not key.is_pressed('f3'):
  if key.is_pressed('f6'):
      activated = not activated
      sleep(0.7)      
  elif activated:
      clicker()
print('\n# Thank you for using!')