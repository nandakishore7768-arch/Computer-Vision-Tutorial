import cv2 

def show_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


path = "image1.webp"

image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found")
else:
    print("Image Loaded Successfully")

show_image("orginal_image", image)

edges = cv2.Canny(image, threshold1=50, threshold2=150)

show_image("edge_detection", edges)

ret, threshold_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

show_image("threshold_image", threshold_image)