from lib import *

def election(Leader_Id,Leader_Port,m):
    if(m.Id_Elect > Leader_Port):
        Leader_Id = m.Id_Elect
        Leader_Port = m.Port_Elect
    else:
        m.Id_Elect = Leader_Id
        m.Port_Elect = Leader_Port