import cv2


img = cv2.imread("billgates.jpg")


cv2.imshow("Image Window", img)

cv2.waitKey()
cv2.destroyAllWindows()
