from module.func.BasicClass import *
import os
import time
import datetime
from datetime import date
import prettytable as pt

valid_tags = {0:["INDI","FAM","HEAD","TRLR","NOTE"],            1:["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV"]         ,2:"DATE"}

def monthToNum(shortMonth):
    return{
            'JAN' : 1,
            'FEB' : 2,
            'MAR' : 3,
            'APR' : 4,
            'MAY' : 5,
            'JUN' : 6,
            'JUL' : 7,
            'AUG' : 8,
            'SEP' : 9, 
            'OCT' : 10,
            'NOV' : 11,
            'DEC' : 12
    }[shortMonth]

def readAndSaveToList(filePath, List, List2):
    
    #read gedcom file
    print(filePath)
    input_ged = open(filePath, "r") 
   # saveFile="output_"+filename+".txt"
   # writeFile = open(saveFile, "w")
    #set flags
    flag_Birth=False
    flag_Death=False
    flag_Married=False
    flag_Divorced=False
    #read each line to input

    for each_input in input_ged:
        # Ensure line is not empty or comments
        if len(each_input)>0 and each_input[:2]!="--":
            each_input=each_input.rstrip("\n")
          #  print(each_input)
            each_input_split=each_input.split()
            # Ensure there're level and tag
            if len(each_input_split)>=2:
                level,tag=int(each_input_split[0]),each_input_split[1]
                # Ensure input is valid
                word_count=2+len(tag)+1
                # Ensure there's desc to process
                if len(each_input_split)>=3:
                    desc=each_input_split[2]
                    # Detect New Individual and create new class
                    if desc=="INDI":
                        ID=tag[0:3]
                        p1=Individuals(ID)
                        List.append(p1)
                    # Detect New Family and create new class
                    if desc=="FAM":
                        ID=tag
                        f1=Families(ID)
                        List2.append(f1)    
                    if tag=="SEX":
                        SEX=desc  
                        p1.Gender=SEX    
                    if tag=="NAME":
                        NAME=each_input[word_count:].strip()
                        p1.Name=NAME
                    if flag_Birth==True and tag=="DATE":
                        B_DAY=int(desc)
                        B_MONTH=int(monthToNum(each_input_split[3]))
                        B_YEAR=int(each_input_split[4])
                        
                        Birthday=datetime.date(B_YEAR,B_MONTH,B_DAY)
                        p1.Age=int ((date.today()-Birthday)/datetime.timedelta (days=1)/365)
                        p1.Birthday=str(Birthday)
                    
                        flag_Birth=False   
                    if flag_Death==True and tag=="DATE":
                        D_DAY=int(desc)
                        D_MONTH=int(monthToNum(each_input_split[3]))
                        D_YEAR=int(each_input_split[4])
                        
                        Death=datetime.date(D_YEAR,D_MONTH,D_DAY)
                        p1.Age=int((Death-Birthday)/datetime.timedelta (days=1)/365)
                        p1.Death=str(Death)

                        flag_Death=False
                    if flag_Married==True and tag=="DATE":
                        M_DAY=int(desc)
                        M_MONTH=int(monthToNum(each_input_split[3]))
                        M_YEAR=int(each_input_split[4]) 
                        MarriedDay=datetime.date(M_YEAR,M_MONTH,M_DAY)
                        f1.Married=str(MarriedDay)
                        
                        flag_Married=False
                    if flag_Divorced==True and tag=="DATE":
                        Div_DAY=int(desc)
                        Div_MONTH=int(monthToNum(each_input_split[3]))
                        Div_YEAR=int(each_input_split[4]) 
                        DivorcedDay=datetime.date(Div_YEAR,Div_MONTH,Div_DAY)
                        f1.Divorced=str(DivorcedDay)
                        
                        flag_Divorced=False
                    if tag=="FAMS":
                        Spouse=desc
                        p1.Spouse=Spouse
                    if tag=="FAMC":
                        Child=desc
                        p1.Child=Child
                    if tag=="HUSB":
                        Husband=desc
                        f1.HusbandID=Husband
                        for each in List:
                            if each.ID==f1.HusbandID: 
                                f1.HusbandName=each.Name      
                    if tag=="WIFE":
                        Wife=desc
                        f1.WifeID=Wife
                        for each in List:
                            if each.ID==f1.WifeID: 
                                f1.WifeName=each.Name
                    if tag=="CHIL":
                        Children=desc
                        f1.Children.append(Children)
                elif len(each_input_split)>=2:
                    if tag=="BIRT":
                        flag_Birth=True
                        p1.Alive="True"
                    if tag=="DEAT":
                        flag_Death=True
                        p1.Alive="False"
                    if tag=="MARR":
                        flag_Married=True
                    if tag=="DIV":
                        flag_Divorced=True


file_name = 'userStory.ged'
filePath = os.path.join(os.getcwd(), "Sample/" + file_name)

# create list for individual and families
individualList=[]
familyList=[]

# read file to create individual and families
if os.path.exists(filePath):
    readAndSaveToList(filePath, individualList, familyList)
else:
    print("File doesn't exist")

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


# Original US10 code
def US10Original(marriageDay, birthday): 
# US10 Check whether the individual is married after 14
    if isinstance(marriageDay, datetime.date) != True:
        if isDataFormat(marriageDay) == False :
            return True
        marriageDay = datetime.datetime.strptime(marriageDay, '%Y-%m-%d')
    if isinstance(birthday, datetime.date) != True:
        if isDataFormat(birthday) == False :
            return True  
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    if ((marriageDay - birthday).days)/365 < 14 :
        return False
    return True


# Modified US10 code
def US10(marriageDay, birthday):
    if isinstance(marriageDay, datetime.date) != True:
        if isDataFormat(marriageDay) == False :
            # Not return true since there are "NA" in the GEDCOM file
            return
        marriageDay = datetime.datetime.strptime(marriageDay, '%Y-%m-%d')
    if isinstance(birthday, datetime.date) != True:
        if isDataFormat(birthday) == False :
            # Not return true since there are "NA" in the GEDCOM file
            return 
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    #Check whether the marriage day is before birthday
    if ((marriageDay - birthday).days)/365 < 0  :
        print("Not even born to get married.")
        return False
    if ((marriageDay - birthday).days)/365 < 14 :
        return False
    return True

import unittest
class TestDateBeforeCurFunc (unittest.TestCase): 
    def test_Equal(self): 
        children=['I01','I02']
        self.assertEqual(US10("1970-07-15","1960-07-15"),False) 
        self.assertEqual(US10("1980-07-15","1960-07-15"),True) 
    def test_NotEqual(self):
        self.assertNotEqual(US10("1970-07-15","1960-07-15"),True)
        children=['I01','I02']
if __name__ == '__main__': 
    unittest.main() 

