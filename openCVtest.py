import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    exit()

while True:
    ret, img = cap.read()

    cv2.imshow('preview', img)

    if cv2.waitKey(10) >= 0 :
        break


cap.release()
cv2.destroyAllWindows()
