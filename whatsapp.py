import pyautogui as pg
import time 
time.sleep(3)

txt = open('Data.txt','r')

a = "Aman is a"

for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')