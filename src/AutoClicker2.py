# AutoClicker v2


print('# F3 - end script\n# F6 - on/off script')


import mouse
import keyboard as key
from time import sleep

activated = False

def m_click():
    mouse.click(button='left')

while not key.is_pressed('f3'):
    if key.is_pressed('f6'):
        activated = not activated
        sleep(0.3)
    elif activated:
        m_click()
print('Bye!')