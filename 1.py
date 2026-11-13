import cv2 

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

image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

show_image("Colored Image", image)
show_image("Black and white image", image1)

saved_status = cv2.imwrite("BW_image.webp", image1)
if saved_status:
    print("Image saved successfully")
else:
    print("Image not saved successfully")

