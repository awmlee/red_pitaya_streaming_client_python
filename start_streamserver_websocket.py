# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:53:46 2020

@author: default_user
"""
#translated from javascript sm.js

import time
from websocket import create_connection  #note the absence of the s at the end of websocket: asyncio has been abstracted abaway with this module 
import gzip  #for unpacking the data from RP's websocket
import requests #for sending the magic url to RP to restart it
import json #for packing and unpacking the parameters going to the websock


class Websocket():
    def __init__(self, socket_url='192.168.11.14'):
        self.socket_url='ws://'+socket_url+'/wss'
        self.start_app_url='http://'+socket_url+'/bazaar?start=streaming_manager'
        self.stop_app_url='http://'+socket_url+'/bazaar?stop=streaming_manage'        
        self.socket_opened=False
        
        
if __name__ == "__main__":
    from websocket import create_connection
    import gzip
    import requests
    import json

    SERVER_ADDR = '192.168.11.14'
    WS=Websocket(SERVER_ADDR)  
    #start server
    try:
        web = requests.get(WS.start_app_url)
        print(web)
    except:
        web = requests.get(WS.stop_app_url)
        print(web)
        web = requests.get(WS.start_app_url)
        print(web)
        
    #open websocket
    ws = create_connection(WS.socket_url)
    #print "Sending 'Hello, World'..."
    #ws.send("Hello, World")
    #print "Sent"
    print("Receiving...")
    result =  ws.recv()
    print("Received '%s'" % result)
    message=json.loads(gzip.decompress(result))
    print(json.loads(gzip.decompress(result)))
    setbits=({"parameters":{"SS_RESOLUTION":{"value":2},"in_command":{"value":"send_all_params"}}})
    setrate= ({"parameters":{"SS_RATE":{"value":800},"in_command":{"value":"send_all_params"}}})
    setdualchan=({"parameters":{"SS_CHANNEL":{"value":3},"in_command":{"value":"send_all_params"}}})
    startcmd=({"parameters":{"SS_START":{"value":1},"in_command":{"value":"send_all_params"}}})
    stopcmd=({"parameters":{"SS_START":{"value":0},"in_command":{"value":"send_all_params"}}})
    ws.send(json.dumps(setbits))
    ws.send(json.dumps(setrate))
    ws.send(json.dumps(setdualchan))
    ws.send(json.dumps(startcmd))
    while(1):
        time.sleep(10)
        print("sleeping")
    #ws.send(json.dumps(stopcmd))
    #ws.close()