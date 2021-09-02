from re import S
from typing import get_origin
import carla
import time
import random
import numpy as np
import cv2
import base64
import websockets

f = open('test1.txt', 'r')

hg_b =list()
hg_b = str(f.readlines())
#print('whowhowhwwho',hg_b)
s = base64.b64decode(hg_b)
#s = base64.decodebytes(hg_b)
print('whowhowhwwho',type(s))



hg_qi = np.frombuffer(s, dtype=np.uint8)
hg_q = hg_qi.reshape((576,1024,3))
hg_r=hg_q[:, :, :3]

cv2.imshow("3",hg_r)

cv2.waitKey(0)

#print ("3",hg_ayy.shape)
#t= np.arange(720,128,4, dtype=np.uint8)
#t =i3
#s= base64.b64encode(i3)
#r= base64.decodestring(s)
#hg_q= np.frombuffer(s, dtype=np.uint8)
#hg_b=base64.b64encode(hg_a)
#hg_c = base64.decodebytes(hg_b)
#hg_q = np.frombuffer(hg_c, dtype=np.uint8)
#hg_r=hg_q[:, :, :3]
#hg_c=base64.decodebytes(hg_b.encode('utf-8'))
#print ("hg:3",hg_c.shape)
#cv2.imshow("2",i2)

#cv2.imshow("3",hg_r)#i4)

#cv2.waitKey(1)


