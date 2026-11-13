import cv2 
import numpy as np 

def show_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img1 = np.zeros((300, 300), dtype = "uint8")
img2 = np.zeros((300, 300), dtype = "uint8")

cv2.circle(img1, (15, 10), 150, 120, -1)
cv2.circle(img2, (250, 250), 250, 255, -1)

bitwise_not = cv2.bitwise_not(img1)
bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)

show_image("bitwise_and", bitwise_and)
show_image("bitwise_or", bitwise_or)
show_image("bitwise_not", bitwise_not)
