import cv2

face_cascade = cv2.CascadeClassifier("haarcascade xml file/haarcascade_frontalface_default")

camera = cv2.VideoCapture(0)

while True:
    ret, Frame = camera.read()

    if ret:
        frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
        detect_faces =  face_cascade.detectMultiScale(frame, 1.1, 5)

        for (x,y,w,h) in detect_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(frame, "Face Detected", (x, y-30), cv2.FONT_HERSHEY_COMPLEX,0.7, 12, color = (0, 0, 255))
        cv2.imshow("Faces Detected", Frame)
        if cv2.waitKey(1) == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
