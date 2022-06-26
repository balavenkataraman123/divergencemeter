import cv2
import numpy as np
image = cv2.imread("nixietube.jpg")
while True:
    cv2.imshow("image", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
num = 0
startxcoord = 0
for i in range(3):
    startycoord = 0
    for j in range(7):
        imgg = image[int(startxcoord):int(startxcoord + 112.333333333), int(startycoord):int(startycoord + 87.4285714286)]
        imggres = cv2.resize(imgg, (87,112), interpolation=cv2.INTER_AREA)
        imggres[np.where((imggres>=[170,170,170]).all(axis=2))] = [0,0,0];
        cv2.imshow("image", imggres)
        if cv2.waitKey(5) & 0xFF == 27:
            break
        if num >= 10:        
            cv2.imwrite(str(num-10) + ".jpg" ,imggres)
        startycoord += 87.4285714286
        num += 1
    startxcoord += 112.333333333

