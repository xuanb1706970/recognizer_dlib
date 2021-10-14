import cv2
import os

def another_image(path):
    array_image = []
    for i in os.listdir(path):
        path_fl = path + '/' + i
        print(path_fl)
        num_path = len(os.listdir(path_fl))
        for j in os.listdir(path_fl):
            print(j)
            if num_path < 4:
                path_image = path_fl + '/' + j
                print(path_image)
                image = cv2.imread(path_image)
                another_1 = cv2.flip(image, 1)
                another_2 = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
                another_3 = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
                array_image.append(image)
                array_image.append(another_1)
                array_image.append(another_2)
                array_image.append(another_3)

                if os.path.exists(os.path.join('data_more', str(i))) == False:
                    os.mkdir(os.path.join('data_more', str(i)))

                for img in array_image:
                    path = 'data_more' + '/' + str(i)
                    _, _, files = next(os.walk(path))
                    file_count = len(files)
                    cv2.imwrite(os.path.join(path + "/" + 'User.' + str(i) + '.' + str(file_count+1) + '.jpg'),img)
                cv2.imshow('another_1', another_1)
                cv2.imshow('another_2', another_2)
                cv2.imshow('another_3', another_3)
                cv2.imshow('faces', image)
                cv2.waitKey()
                cv2.destroyAllWindows()

if __name__ == "__main__":
    another_image('data_num')