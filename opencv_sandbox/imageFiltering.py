import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("images/Me.jpg", 0) # 440 x440
kernel = np.ones((7,7),np.float32)/(7*7)
dst = cv.filter2D(img,-1,kernel)

img_smooth = cv.GaussianBlur(img,(11,11),0)

plt.subplot(121),plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst),plt.title('Averaging/Box Filter')
plt.xticks([]), plt.yticks([])
plt.show()
plt.close()
plt.subplot(121),plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(123), plt.imshow(img_smooth),plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])
plt.show()

# wait indefinitely until any key is pressed
cv.waitKey(0)
cv.destroyAllWindows()