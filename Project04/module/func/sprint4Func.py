
# coding: utf-8

# In[ ]:

import os
import sys
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from func.BasicClass import *
from func.sprint1Func import *


#US_38_List upcoming birthdays
def US38_upcomingBirthdays(pp):
        currentYear = str(datetime.date.today().year)
        nextYear = str(datetime.date.today().year+1)
        if pp.Birthday[5:7] == '01':  #if the birthday is on January, it's possible that occurs 30 days later from December
            birthString = pp.Birthday.replace(pp.Birthday[:4], nextYear)
            birthday = datetime.datetime.strptime(birthString, "%Y-%m-%d").date()
        else:
            birthString = pp.Birthday.replace(pp.Birthday[:4], currentYear)
            birthday = datetime.datetime.strptime(birthString, "%Y-%m-%d").date()
        today = datetime.datetime.now().date()
        iterval = birthday - today
        if datetime.timedelta(days = 0) <= iterval <= datetime.timedelta(days=30):
            #print(pp.ID,pp.Name, birthday)
            return True
        
#US_39_List upcoming anniversaries
def US39_upcomingAnniversaries(fm):
    currentYear = str(datetime.date.today().year)
    nextYear = str(datetime.date.today().year+1)
    if fm.Married[5:7] == '01':
        marriedString = fm.Married.replace(fm.Married[:4], nextYear)
        marriedDay = datetime.datetime.strptime(marriedString, "%Y-%m-%d").date()
    else:
        marriedString = fm.Married.replace(fm.Married[:4], currentYear)
        marriedDay = datetime.datetime.strptime(marriedString, "%Y-%m-%d").date()
    today = datetime.datetime.now().date()
    iterval = marriedDay - today
    if datetime.timedelta(days = 0) <= iterval <= datetime.timedelta(days=30):
        #print(fm.ID, marriedDay)
        return True
    
def US29(ID, Name ,Alive):
    if Alive=='False':
        return True

def US30(ID, Divorced, HusbandID, WifeID, individualList):
    if Divorced=='NA':
        for pp in individualList:
            if HusbandID==pp.ID and pp.Alive=="True":
                return True
            if WifeID==pp.ID and pp.Alive=="True":
                return True


def ListMultipleBirths(indlst):
    
    #This function is to list people who have the same birthday (User Story 32)
    
    dictBirths = {}
    result = []
    
    # Using dict to record birthday
    for p in indlst:     
        if p.Birthday in dictBirths.keys():
            dictBirths[p.Birthday].append(p.ID)
        else:
            dictBirths[p.Birthday] = []
            dictBirths[p.Birthday].append(p.ID)
    
    # add the person into result if their birthday
    for dbirth, deach in dictBirths.items():
        if len(deach) >= 2:
            for eID in deach:
                each = getItemByID(indlst, eID)
                result.append(each)

    
    return result

def ListLivingSingle(indlst):

    #This function is to list people who is single and age more than 30 (User Story 31)

    result = []
    
    for p in indlst:
        
        if p.Alive == "True" and p.Spouse == "NA" and p.Age > 30 and p.Child == "None":
            
            result.append(p)
            
    return result 


def US35(day):
    if day!='NA':
        date=datetime.datetime.strptime(day, '%Y-%m-%d')
        if (datetime.datetime.now()-date).days<=30:
            return True
    return False

def US36(day):
    if day!='NA':
        date=datetime.datetime.strptime(day, '%Y-%m-%d')
        if (datetime.datetime.now()-date).days<=30:
            return True
    return False