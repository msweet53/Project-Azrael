# Project Azrael

# Planning
## Goal
Our goal for this project is to create a multiple stage miniature rocket that when it reaches its apex, turns into a glider and can be controlled remotely, take pictures, and land safely with all non-disposable components.
## What we will need:
For this project, we are going to use model rocket engines to propel our rocket. There will be a raspberry pi onboard the rocket that we will use to take pictures, and stream video of descent down to our controller. Our controller will be made up out of a raspberry pi, touchscreen display, and joysticks. We will use a router to connect both pis allow the streaming of video and saving of pictures on descent. We will also need batteries in order to power the pi as it is in the air. 
## Challenges:
We will need to learn how to use the router that we have to connect the two pis together and stream video from one to another. This is going to be rather challenging because we have never studied this before. 
It is also going to be challenging to find a way to efficiently make disposable rocket stages without high cost for each launch. We will need to figure out how to use cheap materials for our disposable stages.
## Weekly Planning:
Feb 1-8: Finish CAD and get model printed, begin work on rocket software engineering.

Feb 9-15: Begin attempts to use wifi router to communicate with pi at extreme distances, if this fails, begin brainstorming an RC solution.

Feb 16-23: Finish rocket staging python software.

Feb 24- Mar 1: Finish camera software (with wifi video streaming to home base).

Mar 2-8: Finish internal rocket software, begin preperation for launch and control software.

Mar 9-15: Finish control software and figure out launch.

Mar 16-23: Prepare for testing.

Mar 23-31: Finish testing/repairs.

April 1: Final launch (conveniently April fools day.)

## Bill of Materials:
2 Raspberry Pi

Raspberry Pi Screen

Control Joysticks

WiFi router

Battery for rocket fuses and relay

Accelerometer

2 Servos

Pi Camera

Material for parachute

C6-5 Model rocket engines and fuses

Access to 3d printer, lazer cutter, and necessary materials (acyrilic, ABS filament)

A base to launch the rocket from
## Hardware Communications
Our plan is to have Azreal's (the rocket's) descent remotely controlled with a parachute by another Pi that we are calling "home base". Home base and Azrael (home base being the controller, and azrael being the rocket) will communicate through a WiFi router. Home base will receive video transmission from Azrael, and Azrael will receive remote control commands from Home Base. Home base will also be able to send commands to take pictures that will be saved to Azraels SD card. Azreal will send a notification to home base when it reaches the apex of its flight, in case it is not visible in the video stream. 

## Risk Mitigation
We are going to make a station that holds the rocket in place so we can test the rocket's features without launching it into the sky. We will be able to see if the top and bottom of the rocket detatch properly and the tube that keeps gas from getting to the raspberry pi works. We will also be doing a test launch to make sure that nothing will go wrong when the electronics are on. We will launch the rocket in a large open field so it cant do any damage if something goes wrong.

# Design and Manufacturing
## CAD
![ISO EXPLODE](https://github.com/msweet53/Project-Azrael/blob/main/Images/AsraelISOexploded.png)
![ISO](https://github.com/msweet53/Project-Azrael/blob/main/Images/AzraelISO.png)
![Azrael](https://github.com/msweet53/Project-Azrael/blob/main/Images/Azrael1.png)
Here you can find the full assembly for our rocket in OnShape: https://cvilleschools.onshape.com/documents/2a45bfd6e5696b3383110766/w/5fe0dde40c637c081121e03b/e/437919c00aa1a2b2d322f726?renderMode=0&uiState=61f2cd65e31cce2007406903

## Figured out Streaming over Wifi (Mar. 10)
Despite behing behind schedule, we have figured out how to stream video from our small pi, to our large pi using the pi camera and VLC. This stream has a lot of delay and buffer freezing, so we have decided that we will not be using this as reliable data when steering our rocket back to home. 
The command we run on the rockets pi is: raspivid -o - -t 0 -n -w 320 -h 200 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
and we use vlc on the large pi to directly connect to the stream with the proper ip and port.

## Figured out running the client VLC script in the background with python. (Mar. 16)
We have succesfuly figured out how to run the client side VLC command in the background using a python file. We have this running on startup using services right now. 
We used this python script to be able to run our bash command:

import os

os.system("raspivid -o - -t 0 -n -w 320 -h 200 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264")
