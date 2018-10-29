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


def getDescendantList(fID, familyList):
    
    fmlst = []
    clst = []
    fmlst.append(fID)
    newFamily = True
    while newFamily == True:    
        for fmId in fmlst:
            currfm = getItemByID(familyList, fmId)

            if not currfm:
                continue
            else:
                #family exist
                newFamily = False
                for cId in currfm.Children:
                    
                    # add children
                    if cId not in clst:
                        clst.append(cId) 
                        
                    # check current children is in the family list or not
                    for tp in familyList:
                        if tp.HusbandID == cId or tp.WifeID == cId:
                            if tp.ID not in fmlst:
                                fmlst.append(tp.ID)
                                newFamily = True
    return clst

def IsCorrectGender(wID, hID, individualList):
    """Func for UserStory 21 IsCorrectGender(wID, hID, individualList)"""
    flag = True
    msg=''
    t = getItemByID(individualList, wID)
    if not t:
        msg += "ERROR: FAMILY: US21: " + "Can't find Wife ID: " + wID + " in Data \n"
        flag = False
    else:
        if t.Gender != "F": 
            msg += "ERROR: FAMILY: US21: " + "Wife ID: " + wID + " Gender is not Female\n"
            flag = False
            
    t = getItemByID(individualList, hID)
    if not t:
        msg += "ERROR: FAMILY: US21: " + "Can't find Husband ID: " + hID + " in Data \n"
        flag = False
    else:
        if t.Gender != "M": 
            msg += "ERROR: FAMILY: US21: " + "Husband ID: " + hID + " Gender is not Male\n"
            flag = False            
            
    return flag,msg


def Is_Marriages_descendants(familyList):
    """Func for UserStory 17 Is_Marriages_descendants(familyList)"""
    flag = True
    msg=''
    
    for f in familyList:
        childrenlst = getDescendantList(f.ID, familyList)
        
        if f.WifeID in childrenlst:
            msg += "ERROR: FAMILY: US17: F.ID(" + f.ID+") Wife ID: " + f.WifeID + " marriages to descendants \n"
            flag = False
        if f.HusbandID in childrenlst:
            msg += "ERROR: FAMILY: US17: F.ID(" + f.ID+") Husband ID: " + f.HusbandID + " marriages to descendants \n"
            flag = False       
            
    return flag,msg

def US22(IDset,ID): 
    if ID not in IDset:
        IDset.add(ID)
        return True
    else:
        return False

def US23(individualDict,ID,Birthday): 
    if ID not in individualDict:
        individualDict[ID]=Birthday
    else:
        if individualDict[ID]==Birthday:
            return False
    return True

