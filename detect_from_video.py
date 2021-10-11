import cv2
import dlib
from create_data import read_csv


def detect_vdieo():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cap = cv2.VideoCapture(0)
    recognizer.read('training.yml')
    label_name = read_csv('data_name.csv')
    detector = dlib.get_frontal_face_detector()
    while True:

        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            ID, conf = recognizer.predict(gray[y1:y2, x1:x2])

            label = label_name[ID]

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(img, label, (x1, y1), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

        cv2.imshow('face', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_vdieo()
