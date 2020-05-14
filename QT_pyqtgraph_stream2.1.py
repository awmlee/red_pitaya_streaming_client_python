# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:14:57 2020

@author: awmlee
V1.0 
    #keeping pyqtgraph's objects straight is hard.  Using the 'PlotWidget' example from:
    #import pyqtgraph.examples
    #pyqtgraph.examples.run()
    #This is what we have:
    
    #pyqtgraph_widget is the same as pw in example: type pyqtgraph.widgets.PlotWidget.PlotWidget
    #pdi1 is the same as p1 in the exampl: type pyqtgraph.graphicsItems.PlotDataItem.PlotDataItem

V2.0: Runs, stable.
V2.1: Added GUI variables and update function
"""

from PyQt5 import QtWidgets, uic, QtCore
import pyqtgraph as pg
import sys
import numpy as np
import time
import threading
from rp_stream_threaded import SocketClientThread, ClientCommand, ClientReply


#keeping pyqtgraph's objects straight is hard.  Using the 'PlotWidget' example from:
#import pyqtgraph.examples
#pyqtgraph.examples.run()
#This is what we have:

#pyqtgraph_widget is the same as pw in example: type pyqtgraph.widgets.PlotWidget.PlotWidget
#pdi1 is the same as p1 in the exampl: type pyqtgraph.graphicsItems.PlotDataItem.PlotDataItem

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('stream_server_gui.ui', self)
        
        self.timer = pg.QtCore.QTimer()   #start a timer to get process data
        self.timer.timeout.connect(self.update)
        self.timer.start(0)
        
        #GUI stuff
        self.b1.clicked.connect(lambda:print("Button Function"))
        self.pdi1=self.pyqtgraph_widget.plot() #pyqtgraph.graphicsItems.PlotDataItem.PlotDataItem
        self.pdi2=self.pyqtgraph_widget_2.plot()
        self.lcdNumber_datarate.display(0)
        self.lcdNumber_queuedepth.display(0)
        self.spinBox_dec.valueChanged.connect(self.__update_GUI_data)
        self.spinBox_sampsize.valueChanged.connect(self.__update_GUI_data)
        self.checkBox_channel1.stateChanged.connect(self.__update_GUI_data)
        self.checkBox_channel2.stateChanged.connect(self.__update_GUI_data)

        #GUI variables
        self.GUIdecfactor=self.spinBox_dec.value()
        self.GUIdatamaxval=self.spinBox_sampsize.value()
        self.GUIchannel_1_enabled=self.checkBox_channel1.isChecked()
        self.GUIchannel_2_enabled=self.checkBox_channel2.isChecked()
        
        
        self.timestart=time.time()  #time for frame rate
        self.dataframe=0  #counter for number of data packets
        self.dataframeN=100
        self.LOST=0

        self.QUEUE_DEPTH=1000  
        self.SERVER_ADDR = '192.168.11.14', 8900
        
        #run acquisition in another thread
        #self.rps=rp.rp_stream()   #initialize the RP stream
#        self.timer2 = pg.QtCore.QTimer()   #start a timer to get process data
#        self.timer2.timeout.connect(self.update)
#        self.timer2.start(1)
#        t = threading.Thread(target=self.acquire)
#        t.start()
        self.client = SocketClientThread(self.QUEUE_DEPTH)
        self.client.start()
        #CONNECT connects the socket, starts client.run(), and sets client.connected=1, which
        #run loop is continuous, and sends a constant stream of RECEIVE to fill up the buffer
        self.client.cmd_q.put(ClientCommand(ClientCommand.CONNECT, self.SERVER_ADDR))



    def __update_GUI_data(self):
        if self.spinBox_dec.value()==1: 
            self.GUIdecfactor=1
        if np.mod(self.spinBox_dec.value(),2)==1:
            self.GUIdecfactor= self.spinBox_dec.value()+1
        else:
            self.GUIdecfactor=self.spinBox_dec.value()
        self.GUIdatamaxval=self.spinBox_sampsize.value()
        self.GUIchannel_1_enabled=self.checkBox_channel1.isChecked()
        self.GUIchannel_2_enabled=self.checkBox_channel2.isChecked()
        print('Gui Data being Acquired')
        
    def closeEvent(self, event):
        # do stuff
        print("closing")

    def update(self):
        self.lcdNumber_queuedepth.display(self.client.reply_q.qsize())
        if self.client.reply_q.qsize():
            a=self.client.reply_q.get()
            if a.type==0:  #ERROR
                print(a.data)
                print("ERROR: qsize ",self.client.reply_q.qsize())

                time.sleep(1)
                self.client.cmd_q.put(ClientCommand(ClientCommand.CONNECT, self.SERVER_ADDR))
            if a.type==1:   #DATA
                self.dataframe+=1
                t=a.data['params']['timestamp']
                if (self.GUIchannel_1_enabled):
                    datat=a.data['bytes_data1']
                    self.pdi1.setData(datat[0:self.GUIdatamaxval:self.GUIdecfactor])
                if (self.GUIchannel_2_enabled):
                    datat=a.data['bytes_data2']
                    self.pdi2.setData(datat[0:self.GUIdatamaxval:self.GUIdecfactor])
                self.LOST+=a.data['params']['lostrate']
                self.lcdNumber_lost.display(self.LOST)
                if self.dataframe==(self.dataframeN-1):
                    self.lcdNumber_datarate.display(2**16*self.dataframeN/(time.time()-self.timestart)/1024/1024)
                    self.timestart=time.time() #reset timer
                    self.dataframe=0
                    self.LOST=0
            if a.type==2:  #MESSAGE
                print("MESSAGE: qsize ",self.client.reply_q.qsize())
                print(a.data)

if __name__ == '__main__':         
#    main()


    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

    main = MainWindow()
    main.show()
    sys.exit(app.exec_())