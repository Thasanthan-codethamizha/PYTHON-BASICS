import cv2


img = cv2.imread("billgates.jpg")

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image Window", img)
cv2.imshow("Black Image Window", img2)
cv2.waitKey()
cv2.destroyAllWindows()
