import cv2


img = cv2.imread("billgates.jpg")


img[0, 0] = [255, 255, 255]
print(img)
