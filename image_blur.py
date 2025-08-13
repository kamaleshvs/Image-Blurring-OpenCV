import cv2 

img = cv2.imread('gfg.png')

# Blurring methods
avging = cv2.blur(img, (10,10))
gausBlur = cv2.GaussianBlur(img, (5,5), 0)
medBlur = cv2.medianBlur(img, 5)
bilFilter = cv2.bilateralFilter(img, 9, 75, 75)

# Show all at once
cv2.imshow('Original', img)
cv2.imshow('Averaging', avging)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.imshow('Median Blurring', medBlur)
cv2.imshow('Bilateral Filtering', bilFilter)

cv2.waitKey(0)
cv2.destroyAllWindows()