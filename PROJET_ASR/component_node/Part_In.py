from Lib import *
from component_node.elect import *

def Recevoir_Message(s):
    msg=message()
    m, addr=s.recvfrom(2048)
    msg=pickle.loads(m)
    return msg
    
def Envoyer_Message(m,s):
    s.send(pickle.dumps(m))
    
def Handle_Neighbor(con, add, t, Sortie) :
    while True :
        if t==0 :
            msg = con.recv(1024)
            print(msg.decode())
            if msg.decode()=="TOKEN":
                print(" Vous avez reçu le token")
                print(" Vous avez le droit a la parole")
                print(" Pour libérer la parole, il faut saisir le mot --TOKEN--")
                while True :
                    expression = input("Vous pouvez vous exprimer : ")
                    if expression == "TOKEN" :
                        break
        if t==1 :
            input("Vous etes l'initiateur du token tapez entrer pour le libere")
        Sortie.resume()
        t=0

class Part_In(threading.Thread) :
    
    def __init__(self, port, T, S, ID) :
        threading.Thread.__init__(self)

        self.port = port
        
        self.T = T
        
        self.Sortie =S
        
        self.Leader_Id = ID
        
        self.Leader_Port = port
        
        self.Participant = False
        
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try :
            self.ss.bind(('127.0.0.1',self.port))
        
        except :
            print("Le Sd_In n'arrive pas a s'attacher a l'adresse & au numéro de port")
            sys.exit()
        
        self.ss.listen()
    
    def run(self) :
        self.connexion, self.add = self.ss.accept()
       
        Handle_Neighbor(self.connexion, self.add, self.T, self.Sortie)