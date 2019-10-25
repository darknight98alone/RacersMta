#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
import cv2
from std_msgs.msg import String,Float32
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
# import time
# import threading
from carcontrol import detectline

class image_processing:

  def __init__(self):
    # self.k = 1
    # self.writer = cv2.VideoWriter()
    self.rgbImageSub = rospy.Subscriber("/team1/camera/rgb/compressed",CompressedImage,self.getRgbImage,queue_size=1)
    self.AnglePub = rospy.Publisher("/team1/set_angle",Float32,queue_size=1) # angle of car
    self.CameraAnglePub = rospy.Publisher("/team1/set_camera_angle",Float32,queue_size=1) # angle of camera
    self.SpeedPub = rospy.Publisher("/team1/set_speed",Float32,queue_size=1) # speed of car

  def getRgbImage(self,rosdata):
    np_arr = np.fromstring(rosdata.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    image = detectline(image_np)
    cv2.imshow("RGB", image)
    # if self.k==1:
    #   self.writer = cv2.VideoWriter("/home/phamvandan/catkin_ws/src/test/scripts/output.avi",cv2.VideoWriter_fourcc(*"MJPG"),10,(image.shape[1],image.shape[0]))
    # self.writer.write(image)
    # cv2.imwrite("/home/phamvandan/catkin_ws/src/test/scripts/saved/"+str(self.k)+".jpg",image)
    # self.k = self.k + 1
    cv2.waitKey(3)
    self.setSpeed(10)
    self.setAngle(0)

  def setAngle(self,angle):
    self.AnglePub.publish(angle)

  def setCameraAngle(self,angle):
    self.CameraAnglePub.publish(angle)

  def setSpeed(self,speed):
    self.SpeedPub.publish(speed)


def main():
  rospy.init_node('image_processing', anonymous=True)
  image_processing()
  print("connected...")
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()