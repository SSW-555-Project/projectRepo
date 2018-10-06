import os
import sys
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from func.BasicClass import *

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

