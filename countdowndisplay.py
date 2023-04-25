import datetime
import numpy as np
import cv2
img = np.zeros((112, 87*8 + 60, 3), dtype=np.uint8)
b = datetime.datetime(int(input('year: ')),int(input('month: ')),int(input('day: ')),int(input('hour: ')),int(input('minute: ')),int(input('second: ')),0)
ntubelist = []
for i in range(11):
    ntubelist.append(cv2.imread(str(i) + ".jpg"))
while True:
    a = datetime.datetime.now()
    
    c = b - a 
    seconds = c.total_seconds()
    days = str(int((seconds // (3600*24)) % 100))
    hours = str(int(seconds // 3600) % 24)
    minutes = str(int((seconds % 3600) // 60))
    seconds = str(int(seconds % 60))
    
    if len(hours) == 1:
        hours = '0' + hours
    if len(days) == 1:
        days = '0' + days
    if len(minutes) == 1:
        minutes = '0' + minutes
    if len(seconds) == 1:
        seconds = '0' + seconds


    img[ 0:112, 0:87] = ntubelist[int(days[0])]
    img[ 0:112, 87:87*2] = ntubelist[int(days[1])]


    img[ 0:112, 87*2 + 20 :87*3 + 20] = ntubelist[int(hours[0])]
    img[ 0:112, 87*3 + 20 :87*4 + 20] = ntubelist[int(hours[1])]

    img[ 0:112, 87*4 + 40 :87*5 + 40] = ntubelist[int(minutes[0])]
    img[ 0:112, 87*5 + 40 :87*6 + 40] = ntubelist[int(minutes[1])]

    img[ 0:112, 87*6 + 60 :87*7 + 60] = ntubelist[int(seconds[0])]
    img[ 0:112, 87*7 + 60 :87*8 + 60] = ntubelist[int(seconds[1])]
    cv2.imshow("image", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break        
