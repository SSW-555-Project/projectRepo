import os
import sys
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from func.BasicClass import *
def isDataFormat(date):
    if isinstance(date, str) == True and len(date.split('-')) == 3:
        year, month, day = date.split('-')
        if int(month) > 12:
            return False
        
        if int(day) > 31:
            return False
        
        if day[:].isdigit() and month.isdigit() and year.isdigit(): 
            return True
        else:
            return False
    else:
        return False
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

def US10(marriageDay, birthday):
    # US10 Check whether the individual is married after 14
    # Assume temporarily that this function will be call twice. (husband and wife)
    
    if isinstance(marriageDay, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(marriageDay) == False :
            return True
        marriageDay = datetime.datetime.strptime(marriageDay, '%Y-%m-%d')
    
    if isinstance(birthday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(birthday) == False :
            return True
    
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')

    if ((marriageDay - birthday).days)/365 < 14 :
        return False
    return True


def US15(children):
    # US15 Check whether the family has fewer than 15 siblings
    if len(children)>=15:
        return False
    return True