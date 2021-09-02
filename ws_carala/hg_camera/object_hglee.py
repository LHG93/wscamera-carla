import cv2
import numpy as np

def model_setting(model_location, num_label):
    model_layer = model_location.getLayerNames()
    model_out = [model_layer[i[0] - 1] for i in model_location.getUnconnectedOutLayers()]
    rainbow = np.random.uniform(0, 255, size=(len(num_label), 3))
    return model_layer, model_out, rainbow

def photo_setting(photo_location, model_location, model_out):
    photo_location = cv2.resize(photo_location, None, fx=1.0, fy=1.0)
    height, width, channels = photo_location.shape
    #blob = cv2.dnn.blobFromImage(photo_location, 0.004, (256, 256), (0, 0, 0), False, crop=False)
    blob = cv2.dnn.blobFromImage(photo_location, scalefactor=0.016, size=(288, 320), mean=(0, 0, 0), swapRB=True, crop=False)
    model_location.setInput(blob)
    outs = model_location.forward(model_out)
    return photo_location, height, width, channels, blob, outs
