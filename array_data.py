from detector_faces import detector_face
from create_data import read_csv, write_label
import cv2
import os

def array_train(data_path):
    check = 0
    data = read_csv('labels.csv')
    faces = []
    labels = []
    write_label_csv = []

    for i in os.listdir(data_path):
        path_fl = data_path + '/' + i
        label = int(i)
        print(i)
        write_label_csv.append(i)
        for emp in data:
            if int(emp) == int(i):
                check = 1
                break
            else:
                check = 2
        if check == 2:
            for j in os.listdir(path_fl):
                path_img = path_fl + '/' + j
                img = detector_face(path_img)
                if img is not None:
                    faces.append(img)
                    labels.append(label)

    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels, write_label_csv


