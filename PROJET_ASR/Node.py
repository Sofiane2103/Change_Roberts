from random import randint
from Lib import *
from component_node.Part_In import *
from component_node.Part_Out import *
from component_node.elect import *

PORT_In =int(sys.argv[1]) 
Have_Token=int(sys.argv[2]) # 1 si le noeud a le token , 0 sinon !

TYPE="ELECT"
ID=randint(1,66666)
Leader_ID=ID
Leader_Port=PORT_In
print("Mon ID est : ",ID)
print("Les ports et id du leader sont ",Leader_Port,Leader_ID)

msg = message(TYPE,Leader_ID,Leader_Port)

Sd_Out=Part_Out()

Sd_In =Part_In(PORT_In, Have_Token, Sd_Out, Leader_ID)
Sd_In.start()

Sd_Out.port_next_Neighbor =int(input("Numéro de port du voisin: "))
Sd_Out.m=msg
Sd_Out.start()
