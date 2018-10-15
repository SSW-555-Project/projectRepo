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


def US11_noBigamy(info):    
    Info = sorted(info.items(), key=lambda x: x[1][0])
    for i in range(len(Info)):
        earlier_fmID = Info[i][0]
    #     print(earlier_fmID)
        earlier_HusID = Info[i][1][2]
        earlier_WifeID = Info[i][1][3]
        earlier_Married = datetime.datetime.strptime(Info[i][1][0], "%Y-%m-%d").date()
        if Info[i][1][1] == 'NA':
            earlier_Divorced = datetime.datetime.now().date()
        else:
            earlier_Divorced = datetime.datetime.strptime(Info[i][1][1], "%Y-%m-%d").date()
        for j in range(i+1, len(Info)):
            laterInfo = Info[j]
            later_fmID = laterInfo[0]
            later_HusID = laterInfo[1][2]
            later_WifeID = laterInfo[1][3]
            later_Married = datetime.datetime.strptime(laterInfo[1][0], "%Y-%m-%d").date()
            if laterInfo[1][1] == 'NA':
                later_Divorced = datetime.datetime.now().date()
            else:
                later_Divorced = datetime.datetime.strptime(laterInfo[1][1], "%Y-%m-%d").date()
            if later_Married < earlier_Divorced and earlier_HusID == later_HusID:
                FalseList = [False, earlier_HusID, later_Married, earlier_Divorced]
                yield(FalseList)
                continue
            elif later_Married < earlier_Divorced and earlier_WifeID == later_WifeID:
                FalseList = [False,later_fmID, earlier_fmID, earlier_WifeID, later_Married, earlier_Divorced]
                yield(FalseList)
                continue
            else:
                TrueList = [True]
                yield(TrueList)
                continue



def US13_Sibling_Spacing(fm, indiList):
    siblings = fm.Children
    month8 = datetime.timedelta(days=365) * 8 / 12
    days2 = datetime.timedelta(days=2)
    
    if len(siblings) >=1 :
        for i in range(len(siblings)):
            for j in range(i + 1, len(siblings)):
                A = siblings[i]
                B = siblings[j]
                birthA = datetime.datetime.strptime(getItemByID(indiList,A).Birthday, "%Y-%m-%d").date()
                birthB = datetime.datetime.strptime(getItemByID(indiList,B).Birthday, "%Y-%m-%d").date()
                interval = abs(birthA-birthB)
                if interval > month8 or interval < days2:
                    returnList = [True]
            
                  #"""Using yield so that can return every time in second loop"""
                    yield(returnList)
                    continue
                    
                else:             
                    returnList = [False, A, B]
                    yield(returnList)
                    continue
                    
def US14(fmchild, fmid, individualList):
    from datetime import datetime
    
    num=0
    count=0
    alist=[]
    D={}
    flag=True
    stri=""
#     print(len(fmchild))
    if(len(fmchild)>=5):
        #print((len(fmchild)),">5")
        for a in fmchild:
            num+=1
            #print(a)
            for indi in individualList:
                if(a==indi.ID):
                    bir=datetime.strptime(indi.Birthday, "%Y-%m-%d")
                    alist.append(bir)
#             print(len(alist))
            if(num==len(fmchild)):
#                 print(count,num)
                for birthday in alist:
                    if birthday in D.keys():
                        D[birthday]+=1
                    else:
                        D[birthday]=1
#                 print(D)
                max_v=0
                for val in D.values():
                    if val>max_v:
                        max_v=val
#                 print(max_v)
                if (max_v>=5):
                    stri="ERROR: FAMILY: US14:"+fmid+" "+str(max_v)+" siblings were born at the same time"
#                     print(stri)
                    flag=False
#                     return stri)
#                     return (True,stri)
    return flag,stri


from datetime import datetime
def US09(fHusbandID, fWifeID, fchildID, individualList):
    re_list=[]
    s=""
    flag=True
    if(fchildID!= None):
        dad=fHusbandID
        mom=fWifeID
        child=fchildID
        for ind in individualList:
#             print("outside : "+ind.ID)
            if(dad==ind.ID and ind.Death!="NA"):
#                 print("dad died "+fm.ID)
                dadDeath=datetime.now()- datetime.strptime(ind.Death, "%Y-%m-%d")
                for dad_c in child:
                    for a in individualList:
                        if (dad_c==a.ID):
                            childBirth=a.Birthday
                            indi_period= datetime.now()- datetime.strptime(childBirth, "%Y-%m-%d")
                            if(dadDeath.days-indi_period.days>270):
                                s+="ERROR: INDIVIDUAL: US09:"+dad+" died "+ind.Death+" before 9 months than children birth "+childBirth\
                                +"\n"
                                flag=False
            if(mom==ind.ID and ind.Death!="NA"):
#                 print("mom died "+fm.ID)
                momDeath=datetime.now()- datetime.strptime(ind.Death, "%Y-%m-%d")
                for mom_c in child:
                    for b in individualList:
                         if (mom_c==b.ID):
                            childBirth=b.Birthday
                            indi_period= datetime.now()- datetime.strptime(childBirth, "%Y-%m-%d")
                            if(momDeath.days-indi_period.days>0):
                                s+="ERROR: INDIVIDUAL: US09:"+mom+" died "+ind.Death+" before children birth "+childBirth\
                                +"\n"
                                flag=False
                            
    return flag,s
                    

    



