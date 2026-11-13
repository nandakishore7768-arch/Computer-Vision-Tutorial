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
show_image("original_image", image)

new_image = cv2.line(image, (50, 50), (100, 100), (0, 0, 255), thickness=5)

show_image("new_image", new_image)

new_image1 = cv2.rectangle(image, (50,50), (100, 100), (0, 255, 0), thickness=3)

show_image("rectangle in image", new_image1)

new_image2 = cv2.circle(image, (150, 150), 20, (255, 0, 0), thickness=-1)

show_image("circle in image", new_image2)

new_image4 = cv2.putText(image, "This is a text in this image" , (100, 100), cv2.FONT_HERSHEY_DUPLEX,1.0, color = (0,0,0), thickness = 10)

show_image("text in image", new_image4)