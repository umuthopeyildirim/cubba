# CUBBA - Low Energy Pothole Detection System
## Problem
Considering that we use the roads in the cities we live in, we all deal with potholes on a daily basis. Between 50% and 70% of the roads in big cities such as İstanbul, Ankara, İzmir and Adana are used in a damaged state. On average, slightly more than 50 thousand drivers a year in Turkey experience a problem related to potholes. It could be anything; puncture of the tire can lead to the bending of the rim and deterioration of the shock absorber. The financial cost of the repair of these damages reaches up to approximately 1 billion Turkish liras in Turkey. Beyond a financial hardship, potholes can cause a variety of accidents and problems even for the most experienced drivers. About one-fifth of the 7,000 annual traffic deaths are due to poor roads. Since the recycling rate of spare parts of these vehicles is less than 1%, the precaution that can be taken is to prevent these damages and losses.

## Solution
Our solution is simple, thanks to the camera connected to the Raspberry Pi, the video of the vehicle is recorded along the way. Then this video is classified by deep learning. The detected pit is sent to the website along with the picture and GPS coordinate.

Then, when the pit is detected and approved, the road is connected to the municipality to repair the pit. We report to the relevant department of the municipality. This system also analyzes the road defect and road condition and warns the municipality when it should be repaired. In this way, the municipality both saves money and minimizes material and moral damage to the environment.

## How it works
After Raspberry Pi records the road video and gps coordinates, it splits the road video frame by frame into hours, minutes and seconds. Each frame is saved to the device as a picture.

Every image is converted to OpenCV format. Although Raspberry Pi is a very efficient computer. It's not a powerful computer. Two kinds of Computer Vision algorithms are used. These are commonly used in Image Classification and Object Detection. However, Object Detection is not strong enough to run on Raspberry Pi, I could get a maximum of 3-4 FPS. So I used Image Classification. I uploaded and marked my dataset with Azure Cognitive Services. After the model training is finished, Image Classification deep learning application can work with sample codes and Tensorflow documentation.

## Setup
Follow the codes with Python3.
```bash
$ pip3 install -r requirements.txt
$ python3 main.py
```

## In the Future
- The dataset is not very comprehensive, it covers Turkey's 2-4 km long street roads. So a larger dataset may be efficient.
- It is possible to use a more powerful computer to increase the speed of the application.
- Since I don't have a GPS device, even if I wrote the function, it needs to be rewritten and tested.
- It's not a package software but can be translated easily. If it is production software, it can be coded as a startup as soon as the tool is running.
- Main.py can be overhauled.