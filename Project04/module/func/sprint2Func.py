import os
import sys
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from func.BasicClass import *
from func.sprint1Func import *

def isMaleLastNames(fInfo, ilist):

    familyLastName = getItemByID(ilist, fInfo.HusbandID).Name.split("/")[-2]
    
    for cID in fInfo.Children:
        c = getItemByID(ilist, cID)
        
        if c.Gender == 'M' and c.Name.split("/")[-2] != familyLastName:
            return False
        
    return True

def isParentsNotTooOld(fInfo, ilist):
    
    cHusband = getItemByID(ilist, fInfo.HusbandID)
    cWife = getItemByID(ilist, fInfo.WifeID)
    
    y60 = datetime.timedelta(days=365.25).total_seconds() * 60
    
    y80 = datetime.timedelta(days=365.25).total_seconds() * 80

    
    for cID in fInfo.Children:
        c = getItemByID(ilist, cID)
        
        if (cHusband.getDT_Birthday() - c.getDT_Birthday()).total_seconds() > y80 :
            return False
        
        if (cWife.getDT_Birthday() - c.getDT_Birthday()).total_seconds() > y60 :
            return False
        
    return True


def US10(marriageDay,birthday): 
    
    marriageDay = datetime.datetime.strptime(marriageDay, '%Y-%m-%d') 
    
    birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    
    if ((marriageDay - birthday).days)/365 < 0 :
        return True
    if ((marriageDay - birthday).days)/365 < 14 :
        return False
    else:
        return True

def US15(children):
    # US15 Check whether the family has fewer than 15 siblings
    if len(children)>=15:
        return False
    return True

