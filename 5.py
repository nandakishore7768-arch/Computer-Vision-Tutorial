import cv2 

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'XVID')

recorder = cv2.VideoWriter("myvideo.avi", codec, 30, (frame_width, frame_height))

while True:
    success, frame = camera.read()
    if not success:
        print("Failed to capture image")
    else:
        cv2.imshow(frame)
        if cv2.waitKey(1) == ord('q'):
            break

camera.release()
recorder.release()
cv2.destroyAllWindows()