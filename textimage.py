import cv2
img = cv2.imread('nature.jpg',1)
img2 = cv2.imread('text.png',1)
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
dst = cv2.add(img,img2)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()