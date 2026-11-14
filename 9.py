import cv2 
path = "3-inverted-binary.webp"
path1 = "image1.webp"
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not loaded successfully")
else:
    print("Image loaded successfully")

_, threshold = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)
contours, heirarchy = cv2.findContours(threshold , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 5)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    length = len(approx)

    if length == 3:
        print('Triangle')
        shape = "Triangle"

    if length == 4:
        print("Rectangle")
        shape = "Rectangle"

    if length == 5:
        print("Pentagon")
        shape = "Pentagon"

    if length > 6:
        print("Circle")
        shape = "Circle"

    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    x = approx.ravel()[0] - 20
    y = approx.ravel()[1] - 30
    cv2.putText(image, shape, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, 2)

cv2.imshow("sample image", image)
cv2.imshow("threshold image", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

