import cv2 as cv

img = cv.imread("images/Me.jpg", 0)
#Even if the image path is wrong, it won’t throw any error, but print img will give you None
print("Read image from file ,size:{}x{}",img.shape[1], img.shape[0])
cv.imshow("Me", img)
cv.waitKey(0)
img_smooth = cv.GaussianBlur(img,(11,11),0)
cv.imshow("Smoothed",img_smooth)
cv.waitKey(0)
# img_gray = cv.cvtColor(img_smooth, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", img_gray)

img_edges = cv.Canny(img_smooth, 30, 100)
cv.imshow("Edges", img_edges)
# wait indefinitely until any key is pressed
cv.waitKey(0)
cv.destroyAllWindows()