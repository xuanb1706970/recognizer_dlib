import cv2
import time
import numpy
from array_data import array_train
from create_data import write_label

def update_lbp():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    start = time.time()
    #arrray_train('data') ghi ten file luu tru du lieu cua ban
    faces, labels, write_label_csv = array_train('data')
    recognizer.read('training.yml')
    recognizer.update(faces, numpy.array(labels))
    recognizer.save('training.yml')
    print('Thời gian train', time.time() - start, 'seconds.')
    write_label(numpy.array(write_label_csv))

if __name__ == '__main__':
    update_lbp()