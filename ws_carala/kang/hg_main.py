import cv2
import numpy as np
import object_hglee
import carla
import hg_camera

model_location = cv2.dnn.readNet("/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/Kang_JJang_version1.weights",
                                 "/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/yolov3.cfg")
num_label = []
with open("/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/hglee_nene.names", "r") as f:
    num_label = [line.strip() for line in f.readlines()]
model_layer, model_out, rainbow = object_hglee.model_setting(
    model_location, num_label)

hg_image = hg_camera.csKnHcam.GetCamdata()

'''
i = np.array(hg_image.raw_data)
i2 = i.reshape((720, 1280, 4))
i3 = i2[:, :, :3]
'''

photo_location = hg_image
photo_location = cv2.imread("/home/hglee/Downloads/python_dev_carla/bomin/hg_camera/124918.jpg")
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

indexes = cv2.dnn.NMSBoxes(box, num_2, 0.5, 0.4)
print(indexes)
font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(box)):
    if i in indexes:
        x, y, w, h = box[i]
        label = str(num_label[class_num[i]])
        color = rainbow[class_num[i]]
        cv2.rectangle(photo, (x, y), (x + w, y + h), color, 2)
        cv2.putText(photo, label, (x, y + 30), font, 3, color, 3)


cv2.imshow("Image", photo)
cv2.waitKey(0)
cv2.destroyAllWindows()