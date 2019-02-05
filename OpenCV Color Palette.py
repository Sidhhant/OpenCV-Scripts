# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:45:21 2019

@author: Sidhhant
"""
import cv2
import numpy as np

def emptyF():   
    pass

def main():
    img = np.zeros((512, 512, 3), np.uint8)
    windowName = 'OpenCV BGR Color Palette'
    cv2.namedWindow(windowName)
    cv2.createTrackbar('B', windowName, 0, 255, emptyF)
    cv2.createTrackbar('G', windowName, 0, 255, emptyF)
    cv2.createTrackbar('R', windowName, 0, 255, emptyF)
    while(True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(1) == 27:
            break
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)
        
        img[:] = [blue, green, red]
        print (blue, green ,red)
    
    cv2.destroyAllWindows()    
    
if __name__ == "__main__":
    main()