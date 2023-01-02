from Lib import *

def Envoyer_Message(m,s):
    s.send(pickle.dumps(m))
    

 
class Part_Out(threading.Thread) :
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.m = message()
        self.port_next_Neighbor=0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.__flag = threading.Event()
        self.__flag.clear() #set to false
        
    def run(self) :
        try:
            self.s.connect(('127.0.0.1',self.port_next_Neighbor))
        except:
            print("La partie OUT n'arrive pas a se connecter au noeud voisin !")
            sys.exit()
        
        while True :
            self.__flag.wait()
            self.s.send(b"TOKEN")
            self.__flag.clear()
    
    def resume(self) :
        self.__flag.set()