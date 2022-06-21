import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    if cv2. waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
