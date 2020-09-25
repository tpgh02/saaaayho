import pyautogui as p
import keyboard


number = list(range(1,1001))


height = 300
width = 300
counter = 0

while True:
    if keyboard.is_pressed('z'):
        if not keyboard.is_pressed('z'):
            x, y = p.position()
            counter += 1
            p.screenshot('name{}.png'.format(counter),region=(x-height/2,y-width/2,height,width))
    elif keyboard.is_pressed('x'):
        break