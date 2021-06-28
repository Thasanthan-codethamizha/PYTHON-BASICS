import cv2


img = cv2.imread("billgates.jpg")

img[200:250, 230:319] = [0, 0, 0]

cv2.imshow("Image Window", img)

cv2.waitKey()
cv2.destroyAllWindows()
