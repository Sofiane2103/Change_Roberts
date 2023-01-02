import socket
import threading
import sys
import pickle

class message():
    def __init__(self,T="ELECT", IDE=0, PE=0):
        self.Type=T
        self.Id_Elect=IDE
        self.Port_Elect=PE