# Red Pitaya Steaming Client in Python

## What:
  
  

[Red Pitaya](https://www.redpitaya.com/) is a low cost multipurpose circuit board with high-speed dual-channel ADC/DAC, an FPGA, an ARM linux system with USB and ethernet.  The beta version of the Red Pitaya [image](https://redpitaya.readthedocs.io/en/latest/quickStart/SDcard/SDcard.html) has a built in [Streaming Server](https://redpitaya.readthedocs.io/en/latest/developerGuide/125-10/vs.html) [instructions](https://redpitaya.readthedocs.io/en/latest/appsFeatures/apps-featured/streaming/appStreaming.html).  The Streaming Server is capable of acquiring data at rates of up to 125 MSPS and bit depths of 10,14 or 16 bits depending on the hardware, and streaming it to a client over ethernet.  Red Pitaya provides a sample client called [rpsa_client.exe](https://github.com/RedPitaya/RedPitaya/tree/master/apps-tools/streaming_manager), but this saves data to a wav file or a tpms file.  

This repo provides utilities that can:  
1) Remote start the RP streaming manager and set the ADC options (so you don't have to use the web interface to the Red Pitaya)
2) Receive and unpack the data 

As of 5/14/2020, I'm getting >13 MSPS with 14 bit data in two channels when connected to my RP over wifi (it's much faster over ethernet).  This will allow me to decode video streams, or other high data rate applications.
  
## Why:
  
The rpsa_client.exe was insufficient for data streaming.  


## Supported systems:

In theory, this should work on most operating systems, however it was tested using Python 3.7 using spyder and visual studio code.
  
  
## Dependencies:

```
Need to update
```  
  
## Install:
  
```
Need to update
```
  
## run:
  
```
to start the Streaming Server either:
0) Edit the ip address in the file: start_streamserver_websocket.py 
0a) You can edit some of the streaming options in the file to set the data rate, number of channels acquired, and bit depth acquired
1) python start_streamserver_websocket.py  ###Note:  If this program stops running, the websocket will be closed, and the streaming server will stop

to start streaming data:
0) Edit the ip address in the file: rp_stream_threaded.py
1) python rp_steram_threaded.py
```
  
## To Do:  
  
OMG so much (throws up hands).  Feedback welcome.

## Who:
  
Alan Lee [LongWave Photonics](https://longwavephotonics.com)
  

  
