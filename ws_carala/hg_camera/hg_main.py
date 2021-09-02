import cv2
import numpy as np
import object_hglee
import time

start = time.time()

model_location = cv2.dnn.readNet("/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/yolov3.weights", "/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/yolov3.cfg")
num_label = []
with open("/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/hglee_nene.names", "r") as f:
    num_label = [line.strip() for line in f.readlines()]
model_layer, model_out, rainbow = object_hglee.model_setting(model_location, num_label)

print("time0 :", time.time() - start)
photo_location = cv2.imread("/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/a.jpg") #car.JPG
photo, height, width, channels, nothing, outs = object_hglee.photo_setting(photo_location, model_location, model_out)

class_num = []
num_2 = []
box = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            box.append([x, y, w, h])
            num_2.append(float(confidence))
            class_num.append(class_id)
            
print("time11 :", time.time() - start)
indexes = cv2.dnn.NMSBoxes(box, num_2, 0.5, 0.4)
print(indexes)
font = cv2.FONT_HERSHEY_PLAIN

print("time1 :", time.time() - start)
for i in range(len(box)):
    if i in indexes:
        x, y, w, h = box[i]
        label = str(num_label[class_num[i]])
        color = rainbow[class_num[i]]
        cv2.rectangle(photo, (x, y), (x + w, y + h), color, 2)
        cv2.putText(photo, label, (x, y+30), font, 3, color, 3)
print("time2 :", time.time() - start)

cv2.imshow("Image", photo)
cv2.waitKey(0)
print("time3 :", time.time() - start)
cv2.destroyAllWindows()