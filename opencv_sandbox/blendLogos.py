
import cv2 as cv

#Shree Ram.Thank you for guiding me towards learning about computer vision.
# Computer Vision is amazing.:-)
alpha = 0.5

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

print(''' Simple Linear Blender
-----------------------
* Enter alpha [0.0-1.0]: ''')
input_alpha = float(raw_input().strip())
if 0 <= alpha <= 1:
    alpha = input_alpha
# [load]
img1 = cv.imread("images/object.jpg", 0)
img2 = cv.imread("images/object1.jpg", 0)
src1 = cv.resize(img1,None,fx=0.25, fy=0.125, interpolation = cv.INTER_CUBIC)
src2 = cv.resize(img2,None,fx=0.25, fy=0.125, interpolation = cv.INTER_CUBIC)
cv.imshow("object1", src1)
cv.waitKey(0)
cv.imshow("object2", src2)
cv.waitKey(0)
# [load]
if src1 is None:
    print("Error loading src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)
# [blend_images]
beta = (1.0 - alpha)
dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
# [blend_images]
# [display]
cv.imshow('dst', dst)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()