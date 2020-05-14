# Red Pitaya Steaming Client in Python

## What:
  
  

[Red Pitaya](https://www.redpitaya.com/) is a low cost multipurpose circuit board with high-speed dual-channel ADC/DAC, an FPGA, an ARM linux system with USB and ethernet.  The beta version of the Red Pitaya [image](https://redpitaya.readthedocs.io/en/latest/quickStart/SDcard/SDcard.html) has a built in [Streaming Server](https://redpitaya.readthedocs.io/en/latest/developerGuide/125-10/vs.html) ([instructions](https://redpitaya.readthedocs.io/en/latest/appsFeatures/apps-featured/streaming/appStreaming.html)).  The Streaming Server is capable of acquiring data at rates of up to 125 MSPS and bit depths of 10,14 or 16 bits depending on the hardware, and streaming it to a client over ethernet.  Red Pitaya provides a sample client called [rpsa_client.exe](https://github.com/RedPitaya/RedPitaya/tree/master/apps-tools/streaming_manager), but this saves data to a wav file or a tpms file.  

This repo provides utilities that can:  
1) Remote start the RP streaming manager and set the ADC options (so you don't have to use the web interface to the Red Pitaya)  
2a) Receive and unpack the data  
2b) Receive, unpack and display the data in a GUI  

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

(option 1) to start streaming data:
0) Edit the ip address in the file: rp_stream_threaded.py
1) python rp_stream_threaded.py  

(option 2) to start streaming data in a gui:
0) Edit the ip address in the file:  QT_pyqtgraph_stream2.1.py
1) python QT_pyqtgraph_stream2.1.py
  
rp_stream_threaded is a package that has two classes that implement threaded data receiving and unpacking.  In the __main__ section is a sample implementation of its use.  Running the program from the command line, receives the data stream and prints diagnostic messsages such as the data rate, and the packets 'lost' (a parameter included by the streaming server code).  I flagged the section where the data is available('DATA AVAILABLE HERE!!!').   If this code stops running, check that the streaming server hasn't restarted itself.
  
QT_pyqtgraph_stream2.1.py calls rp_steam_threaded and displays the streaming data in a pyqtgraph.  There are some options for the data display.  The gui was created in QT designer and can be edited. If this code stops running, check that the streaming server hasn't restarted itself.
```
  
## To Do:  
  
OMG so much (throws up hands).  Feedback welcome.

## Who:
  
Alan Lee [LongWave Photonics](https://longwavephotonics.com)
  

  
