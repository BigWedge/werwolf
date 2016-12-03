import registrationLogic


bool jaegerActive, armorActive, seherinActive, hexeActive = False

def setAlive(players[]):
    bool alive = True
    for i in range(0,len(players)):
        players[i].extend(alive)
    return True

def setUpRoles(players[])
    #booleans if every special role is active
    for i in range(0,len(players)):
        if players[i][1] == "Jaeger":
            jaegerActive==True
            """
        elif players[i][1] == "Schlampe":
            jaegerActive==True
            """
        elif players[i][1] == "Seherin":
            jaegerActive==True
        elif players[i][1] == "Armor":
            jaegerActive==True
        elif players[i][1] == "Hexe":
            jaegerActive==True

def jaeger(players[],namen):
    #when jaeger dies, kill someone else
    for i in range(0,len(players)):
        if players[i]==namen:
            players[2]==False
    return True



def armor(players[], namen[]):
    #attach to each person if they are lovers
    bool inLove = True
    for i in range(0,len(players)):
        if players[i][0]==namen[0]:
            players[i].extend(inLove)
        elif players[i][0]==namen[1]:
            players[i].extend(inLove)
        elif True:
            players[i].extend(False)
    return True

def seherin(players[], namen):
    #return true or false if the picked person is a ww
    for i in range(0,len(players)):
        if(namen==players[i][0]):
            if players[i][1]=="Werwolf":
                return True
    return False
"""
def setUpBitch(players[]):
    #attach to everyPerson if there is sleeping anybody, bitchinteger else
    for i in range(0,len(players)):
        players[i].extend(0)
        #also safe which one is the bitch
        if players[i][1]=="Schlampe":
            int bitchInteger=i
            
        

def schlampe(players[], namen):
    #if armor is active we have to save where the bitch sleeps in different spaces
    setUpBitch(players[])
    if armorActive:
        for i in range(0,len(players)):
            if namen==players[i][0]:
                
        players[bitchInteger][4]=namen
    elif not armorActive:
        player[bitchInteger][3]=namen
    return True
"""


#for hexe, ww, daykill
def kill(player[], namen):
    #if we kill someone, we have to check if the jaeger, schlampe, armor are involviert
    for i in range(0,len(players)):
        if namen==players[i]:
            #check for bitch
            """
            if schlampeActive:
                #tried to kill the bitch?
                if i==bitchInteger:
                    return True
                    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
                if armorActive:
                    players[i][0]

                if not armorActive:
                    if not players[i][0]==players[i][3]:
                        players[bitchInteger][2]=False
            """
            #kill the person
            namen[2]=False
            #check for special jaeger
            if player[i][1]=="Jaeger":
                jaeger(players[], namen)

            #get inLove couple
            if armorActive && players[i][3]:
                for j in range(0,len(players)):
                    if players[j][3]:
                        players[j][2]=False
                     
    return True

def hexeHeal(players[], heal):
    if heal:
        retun False
    return True

def hexeKill(players[],namen):
    kill(players[],namen)


    







                
