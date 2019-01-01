import cv2
img = cv2.imread("Me.png")
# print("Read image from file ,size:{}x{}",img.shape[1], img.shape[0])
# cv2.imshow("Mona Lisa", img)
# img_smooth = cv2.GaussianBlur(img,(7,7),0)
# cv2.imshow("Smoothed",img_smooth)

# img_gray = cv2.cvtColor(img_smooth, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscale", img_gray)

# img_edges = cv2.Canny(img_gray, 30, 100)
# cv2.imshow("Edges", img_edges)
