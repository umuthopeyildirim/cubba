#gerekliler
import glob
import os
import shutil
import subprocess

shutil.rmtree("demo")
os.mkdir('demo')
shutil.rmtree("pothole_detected")
os.mkdir('pothole_detected')

#Scriptler
# import capture_camera
import export_video
import classificition
import gps_capture

# Take Every one picture
count = 0
pictures = glob.glob("demo/*.jpg")
picturesLenght = len(pictures)

while(picturesLenght>count):
    classificition.classification("demo/%d.jpg" % count)
    count += 1

