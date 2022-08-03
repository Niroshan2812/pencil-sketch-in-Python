

import cv2

# reading image
img = cv2.imread("Insert your jpg location")
# now we need to convert RGB format to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# NOW invert the grayscale image also called the native image.
#image inversion
invert_img = 255 - gray_img
#Create the pencil sketch by mixing the grayscale image with inverted bluray image
blurrd = cv2.GaussianBlur(invert_img, (21, 21), 0 )
invert_blurrd = 255-blurrd
pencil_skt = cv2.divide(gray_img, invert_blurrd, scale= 256.0)
cv2.imshow("Real image", img)
cv2.imshow("Pencil skerch", pencil_skt)
cv2.waitKey(0)