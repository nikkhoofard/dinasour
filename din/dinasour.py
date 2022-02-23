
import cv2
import numpy as np
import pyautogui 

while True :
  image = pyautogui.locateOnScreen('44ee~1.png')
  image = cv2.cvtColor(np.array(image),cv2.COLOR_BGR2RGB)
  
  
  black_pixel_count = np.sum(image < 100 )
  white_pixel_count = np.sum(image > 100 )
  
  print('black of pixel ', black_pixel_count)
  print('white of pixel ', white_pixel_count)
  
  if black_pixel_count > 4000 and black_pixel_count < 30000 :
        pyautogui.press('up')
        
  if white_pixel_count > 4000 and white_pixel_count < 30000 :
        pyautogui.press('up')
        
  
  cv2.imshow('image',image)
  if cv2.waitKey(25) & 0xff == ord('q'):
      cv2.destroyAllWindows()