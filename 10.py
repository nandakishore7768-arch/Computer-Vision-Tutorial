from ultralytics import YOLO
import cv2 

model = YOLO("yolo26n.pt")
result = model("bus.jpg", conf = 0.05, save = True, verbose = False)[0]
image = cv2.imread("bus.jpg")
for box in sorted(result.boxes, key = lambda b: -float(b.conf[0])):
    name = result.names[int(box.cls)]
    conf = float(box.conf[0])
    x1, y1, x2,y2 = box.xyxy[0].tolist()
    print(f"NAME : {name}")
    print(f"Confidence : {conf}")
    print(f"box location : {x1, y1, x2, y2}")

    
    cv2.putText(image, str(name), (int(x1), int(y1-40)), cv2.FONT_HERSHEY_COMPLEX, 1, color = (0, 0, 255), thickness=3)
    cv2.putText(image, str(round(conf, 2)), (int(x1), int(y1-20)), cv2.FONT_HERSHEY_COMPLEX, 1, color = (0, 0, 255), thickness=3)
    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color = (255, 0, 0), thickness=3)

cv2.imshow("modelled_image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()