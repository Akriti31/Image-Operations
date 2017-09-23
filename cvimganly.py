
import numpy as np
import cv2

img= cv2.imread('jpic.png',cv2.IMREAD_COLOR)

roi=img[231:285,378:434]
#print roi
img[131:185,348:404]=roi

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
