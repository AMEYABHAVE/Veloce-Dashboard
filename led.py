import board
import neopixel
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 30)

pixels[0] = (255,255,0)
pixels[1] = (0,255,0)
pixels[2] = (0,255,0)
pixels[3] = (0,255,0)
pixels[4] = (255,0,0)
pixels[5] = (255,0,0)
pixels[6] = (255,0,0)
pixels[7] = (0,0,255)
pixels[8] = (0,0,255)
pixels[9] = (0,0,255)

'''
while 1:
    
    for x in range(0, 10):
        pixels[x] = (255, 0, 0)
        sleep(0.1)
        
    for x in range(10, 0, -1):
        pixels[x] = (0, 0, 0)
        sleep(0.1)
        
    for x in range(0, 10):
        pixels[x] = (0, 255, 0)
        sleep(0.1)
        
    for x in range(10, 0, -1):
        pixels[x] = (0, 0, 0)
        sleep(0.1)
        
    for x in range(0, 10):
        pixels[x] = (0, 0, 255)
        sleep(0.1)
        
    for x in range(10, 0, -1):
        pixels[x] = (0, 0, 0)
        sleep(0.1)
'''
        
        