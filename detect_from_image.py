import cv2
import os
import dlib
from create_data import read_csv

def detect_image(img):
    data = read_csv('data_name.csv')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('training.yml')
    detector = dlib.get_frontal_face_detector()
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) == 0:
        return "Hình ảnh không có khuôn mặt"

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        ID, conf = recognizer.predict(gray[y1:y2,x1:x2])
        label = data[ID]

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.putText(image, label, (x1, y1), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    cv2.imshow('img', image)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    path = 'Aaron_Patterson_0001.jpg'
    detect_image(path)