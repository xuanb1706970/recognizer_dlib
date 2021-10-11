import dlib
import cv2

#Dò tìm khuôn mặt
def detector_face(img):
    detector = dlib.get_frontal_face_detector()
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) == 0 or len(faces) >= 2:
        return None
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        if (x1 < 0) or (x2 < 0) or (y1 < 0) or (y2 <0):
            return None
        else:
            return gray[y1:y2, x1:x2]

