import os
import sys
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from func.BasicClass import *
from func.sprint1Func import *
from func.sprint2Func import *

def US20(WifeID, HusbandID, familyList):
    s=""
    wID=WifeID
    hID=HusbandID
    flag=True
    for each in familyList:
        
        father=each.HusbandID
        mother=each.WifeID
        #print("==",father, mother)
        for second in familyList:
            if father in second.Children:
                if wID in second.Children:
                    flag=False
                    #print("dad",wID,father)
                    #print("dad Wrong", "W:"+wID, "H:"+hID, each.ID, second.ID, "f="+father, "m="+mother)
                    #print(second.ID)
                    s+="ERROR: FAMILY: US20: "+second.ID+": cannot marry because they are nieces or nephews" 
                    
            if mother in second.Children:
                if hID in second.Children:
                    flag=False
                    #print("mom",hID,mother)
                    #print("mom Wrong", "W:"+wID, "H:"+hID, each.ID, second.ID, "f="+father, "m="+mother)
                    #print(second.ID)
                    s+="ERROR: FAMILY: US20: "+second.ID+": cannot marry because they are nieces or nephews"
    return flag,s
        



def US24(WifeName, HusbandName, Married, famID, familyList):
    wName=WifeName
    hName=HusbandName
    fID=famID
    flag=True
    s=''
    if Married!="NA":
        Mday=datetime.datetime.strptime(Married, '%Y-%m-%d')
        for each in familyList:
            if fID!=each.ID:
                if each.WifeName==wName and each.HusbandName==hName:
                    if each.Married!="NA":
                        mmday=datetime.datetime.strptime(each.Married, '%Y-%m-%d')
                        if Mday==mmday:
                            s+="ERROR: FAMILY: US24: "+each.ID+" and "+fID+" has the same spouses by name and the same marriage date"
                            flag=False
                    
    return flag,s



