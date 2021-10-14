from detector_faces import detector_face
from create_data import read_csv
import cv2
import os

def array_train(data_path):
    faces = []
    labels = []
    write_labels = []
    for i in os.listdir(data_path):
        path_fl = data_path + '/' + i
        label = int(i)
        write_labels.append(i)
        for j in os.listdir(path_fl):
            path_img = path_fl + '/' + j
            image = detector_face(path_img)
            if image is not None:
                faces.append(image)
                labels.append(label)
                cv2.imshow('faces', image)
                cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels, write_labels

def array_update(data_path):
    check = 0
    data = read_csv('labels.csv')
    write_label = []
    faces = []
    labels = []
    for i in os.listdir(data_path):
        path_fl = data_path + '/' + i
        label = int(i)
        write_label.append(i)
        for emp in data:
            if int(emp) == int(i):
                check = 1
                break
            else:
                check = 2
        if check == 2:
            for j in os.listdir(path_fl):
                path_img = path_fl + '/' + j
                image = detector_face(path_img)
                if image is not None:
                    faces.append(image)
                    labels.append(label)
                    cv2.imshow('faces', image)
                    cv2.waitKey(1)
            cv2.destroyAllWindows()

            return faces, labels, write_label







