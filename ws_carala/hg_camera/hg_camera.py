#!usr/lib/env/python

import carla
import time
import random
import numpy as np
import cv2
import base64

im_width = 1280
im_heigt = 720
global i3data
i3data=[]

class csKnHcam:
    #global
    gdata = ""
    def __init__(self):
        self.i3data =None

    def GetCamdata(self):
        #return self.json_str
        return csKnHcam.i3data

    def process_img(image):

        image.convert(carla.ColorConverter.Raw)
        print('hghghdsfkjdsflkdsjlfdsjf',image)
        #hg_a=image.raw_data
        #hg_a=image.raw_data
        #hg_b=base64.b64encode(hg_a)
        #print(hg_b)
        #hg_c=base64.b64decode(hg_b)

        #i = np.array(hg_c)
        #print ("hg_1", i.shape)

        i = np.array(image.raw_data)
        print ("1", i.shape)
        print ("")
        print(i)

        i2 = i.reshape((720,1280,4))
        print ("2", i2.shape)


        i3 = i2[:, :, :3]
        print ("3",i3.shape)
        print('h4333333333',i3)
        print ("")
        
        #hg_a=i3
        #print ("3",hg_ayy.shape)
        #hg_b=base64.b64encode(hg_a)
        #hg_c=base64.decodebytes(hg_b)
        #hg_q=np.frombuffer(hg_c,dtype=np.float64)
        #print ("hg:3",hg_c.shape)
        # cv2.imshow("2",i2)
        # cv2.imshow("3",i3)
        #cv2.imshow(hg_c)
        # cv2.waitKey(1)
        global i3data
        i3data=[]

        csKnHcam.i3data = i3
        i3data = i3
        return i3
        

actor_list = []
try:

    vehicle_num = 267

    client = carla.Client("localhost", 2000)
    client.set_timeout(2.0)
	#world = client.load_world('Town04')
    world = client.get_world()

    blueprint_library = world.get_blueprint_library()
    vehicle = world.get_actors().find(vehicle_num)
    print('fkdjffdslkfldskfld;skfl;dskf')
    cam_bp = blueprint_library.find('sensor.camera.rgb')
    cam_bp.set_attribute('image_size_x','1280')
    cam_bp.set_attribute('image_size_y','720')
    print("cam_bp")
    cam_bp.set_attribute('fov','90')
    cam_bp.set_attribute('sensor_tick','0.0')
    cam_bp.set_attribute('shutter_speed','10.0')
    camera_sp = carla.Transform(carla.Location(x=2, z=2))
    camera = world.spawn_actor(cam_bp, camera_sp, attach_to = vehicle)
    actor_list.append(camera)
    camera.listen(lambda data: csKnHcam.process_img(data))
    print(csKnHcam.GetCamdata)
    print("cam_bpwqd")
    #camera.listen(lambda data: data.save_to_disk('/home/hglee/cam_hg/%.6d.jpg' % data.frame))
    #time.sleep(1000000)
    


finally:

    for actor in actor_list:
        actor.destroy()
    
    print ('all actor cleaned up')
