import pyautogui
import time



while True :
    im = pyautogui.screenshot()
    screen = im.getpixel((540,226))
    
    x1 = im.getpixel((817,273))                           
    x2 = im.getpixel((830,273))
    x3 = im.getpixel((800,273))
    x4 = im.getpixel((821,273))
    
    y1 = im.getpixel((820,226))
    y2 = im.getpixel((818,226))
    y3 = im.getpixel((817,226))
    y4 = im.getpixel((805,226))
    
    if screen[0] == 255 :
        if x1[0] != 255 or x2[0] != 255 or x3[0] != 255 or x4[0] != 255 or y1[0] != 255 or y2[0] != 255 or y3[0] != 255 or y4 [0] != 255 :
            pyautogui.press('space')
            time.sleep(0.00001)
    else :
         if x1[0] != 0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] !=0 or y2[0] != 0 or y3[0] != 0 or y4 [0] != 0 :
             pyautogui.press('space')
             time.sleep(0.00001)
             
             




