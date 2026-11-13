import cv2 
import numpy as np 

def show_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


path = "image1.webp"

image = cv2.imread(path)

if image is None:
    print("Image not found")
else:
    print("Image Loaded Successfully")

blurred_image = cv2.GaussianBlur(image, (9,9), 0)
blurred_image1 = cv2.medianBlur(image, 11)

sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_image =  cv2.filter2D(image, -1, sharpening_kernel)

show_image("Orginal_image", image)
show_image("Blurred_image", blurred_image)
show_image("Median Blurred image", blurred_image1)
show_image('Sharpened image', sharpened_image)