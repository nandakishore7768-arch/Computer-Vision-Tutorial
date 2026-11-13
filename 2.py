import cv2

def show_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

image = cv2.imread("image1.webp")

if image is None:
    print("image not loaded")

else:
    print("Image found")

resized_image = cv2.resize(image, (900, 400))
cropped_image = image[100:200, 100:200]
center_width, center_height = image.shape[0]/2, image.shape[1]/2
rotation_matrix = cv2.getRotationMatrix2D((center_width, center_height), angle=90, scale = 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, image.shape[:2])
flipped_horizontal = cv2.flip(image, 1)
flipped_vertical = cv2.flip(image, 0)
flipped_both = cv2.flip(image, -1)

show_image("original_image", image)
show_image("Resized_image", resized_image)
show_image("cropped_image", cropped_image)
show_image("Rotated_image", rotated_image)
show_image("Horizontal_flip", flipped_horizontal)
show_image("Vertical_flip", flipped_vertical)
show_image("Horizontal + Vertical flip", flipped_both)

