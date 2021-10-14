import cv2
import time
import numpy
from array_data import array_train
from create_data import write_label

def train_lbp():
    recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 130.0)
    start = time.time()
    faces, labels, write_labels_csv = array_train('data_num')
    # arrray_train('data') ghi ten file luu tru du lieu cua ban
    recognizer.train(faces, numpy.array(labels))
    recognizer.save('training_123.yml')
    print('Thời gian train', time.time() - start, 'seconds.')
    write_label(write_labels_csv)

if __name__ == "__main__":
    train_lbp()