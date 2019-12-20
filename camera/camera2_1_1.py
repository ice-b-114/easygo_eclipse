import cv2
import time
import datetime
import os

img_counter = 0
path1 = "C:\\Users\\JSKJ\\Desktop\\"
path2 = "C:\\Users\\Administrator\\Desktop\\skl_train\\train_jpg\\"
path3 = "C:\\Users\\Administrator\\Desktop\\fruit\\3ceng\\"
path4 = "C:\\Users\\Administrator\\Desktop\\pic_1\\"
time_flags_1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
time_flags_2 = str(int(time.time()))[7:]


def run(camera_obj, path):
    cam = cv2.VideoCapture(int(camera_obj))
    cv2.namedWindow("camera2.0.0")
    global img_counter
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    while True:
        ret, frame = cam.read()
        cv2.imshow("camera2.0.0", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            cam.release()
            cv2.destroyAllWindows()
            return False
        elif k % 256 == 32:
            # SPACE pressed
            img_name = path + time_flags_1 + str(img_counter).zfill(4) + '.jpg'
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            break
    cam.release()
    cv2.destroyAllWindows()
    return True


def run2(camera_obj, path):
    cam = cv2.VideoCapture(int(camera_obj))
    cv2.namedWindow("camera2.0.0")
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    global img_counter
        
    ret, frame = cam.read()
    cv2.imshow("camera2.0.0", frame)
    # cv2.waitKey(3000)
    img_name = path + time_flags_1 + str(img_counter).zfill(4) + '.png'
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    return True


def go():
    if run(0, path2):
        run(1, path3)
        # run(2, path3)
        # run(3, path4)
        

if __name__ == '__main__':
    for i in range(1,100):
        date = time.strftime('%m.%d', time.localtime(time.time()))
        temp = os.path.join(path1,date,str(i))
        if not os.path.exists(temp):
            os.makedirs(temp)
            path1 = temp
            break
        else:
            i+=1
    while True:
        run(1, path1)
        # run(0,path2)
        # go()
