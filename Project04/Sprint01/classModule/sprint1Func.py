import datetime

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

def isBirthBeforeDeath(birthday, deathday):
    # US03 Birth should occur before death of an individual
    

    if isinstance(birthday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(birthday) == False :
            return False
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')


    
    if isinstance(deathday, datetime.date) != True:
        #msg = "The type of deathday is not datetime"
        if isDataFormat(deathday) == False :
            return False
        deathday = datetime.datetime.strptime(deathday, '%Y-%m-%d')
     

    if(deathday - birthday).total_seconds() > 0 :
        return True
    else:
        return False

def isMarriageBeforeDeath(marriageday, deathday):
    # US05 Marriage should occur before death of either spouse
    # Assume temporarily that this function will be call twice. (husband and wife)

    if isinstance(marriageday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(marriageday) == False :
            return False
        marriageday = datetime.datetime.strptime(marriageday, '%Y-%m-%d')
    
    if isinstance(deathday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(deathday) == False :
            return False
        deathday = datetime.datetime.strptime(deathday, '%Y-%m-%d')

    if(deathday - marriageday).total_seconds() > 0 :
        return True
    else:
        return False
def isDateBeforeCur(day):
    # US01 Every dates should be earlier before current date
    if day!='NA':
        date=datetime.datetime.strptime(day, '%Y-%m-%d')
        if (date-datetime.datetime.now()).days>0:
            return False
    return True


def isDivorceBeforeDeath(divorceday, deathday):
    # US06 Check whether divorce date is before death date or not
    # Assume temporarily that this function will be call twice. (husband and wife)

    if isinstance(divorceday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(divorceday) == False :
            return True
        divorceday = datetime.datetime.strptime(divorceday, '%Y-%m-%d')
    
    if isinstance(deathday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(deathday) == False :
            return True
    
        deathday = datetime.datetime.strptime(deathday, '%Y-%m-%d')

    if(divorceday - deathday).total_seconds() > 0 :
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















def birthBFmarried(fmID, fmDay,iBirth):
    if fmDay == 'NA':
        return False
    
    birth = datetime.datetime.strptime(iBirth, "%Y-%m-%d")
    marrDay = datetime.datetime.strptime(fmDay, "%Y-%m-%d")
    ID = fmID
    
    if (birth - marrDay).total_seconds() > 0:
        print(f"ERROR: FAMILY: {ID} US02: Birth day '{birth}' after Married day: '{marrDay}'")
        return False
    else:
        print(f"FAMILY: US02: {ID} married day '{marrDay}' is valid")
        return True
    
def ageLess150(indi):
    if  indi == None:
        print("No individual can be tested")
        return False

    else: 
        ID = indi.ID
        Age = indi.Age
        if Age > 150:
            #                     raise ValueError('The age is over 150!')
            print(f"ERROR: INDIVIDUAL: US07: {ID} age '{Age}' is over 150!")
            return False
        else:
            print(f"INDIVIDUAL: US07 {ID}'s age '{Age}' is less than 150 ")
            return Age < 150
def US04(famID,Date_married,Date_divorced):
    from datetime import datetime
    if(Date_married!="NA" and Date_divorced!="NA"):
        result=datetime.strptime(Date_divorced, "%Y-%m-%d")-datetime.strptime(Date_married, "%Y-%m-%d")
        #print(Date_divorced,Date_married)
        #print(result.days)
        if(result.days<0):
            print("Error Family: US04 ",famID," : Marriage",Date_married, "after divorce",Date_divorced )
        else:
            print("Family: US04 ",famID," : Marriage",Date_married, "before divorce",Date_divorced, "is valid" )
            
            
def US08(iList,famID,ID,married_date,divorced_date):
    from datetime import datetime
    if(married_date!="NA" and divorced_date!="NA"):
        for indi in iList:
            indiid=indi.ID
            married_period= datetime.now()- datetime.strptime(married_date, "%Y-%m-%d")
            indi_period= datetime.now()- datetime.strptime(indi.Birthday, "%Y-%m-%d")
            divorced_period= datetime.now()- datetime.strptime(divorced_date, "%Y-%m-%d")
            #print(married_period.days, indi_period.days, divorced_period.days)
            if(indi_period.days<married_period.days and indi_period.days>=divorced_period.days-270):
                print("Error Individual ID: US08 ",indiid,": birthday:", indi.Birthday, "is born before parents marriage: ",married_date )
            elif(indi_period.days>=married_period.days and indi_period.days<divorced_period.days-270):
                print("Error Individual ID: US08 ",indiid,": birthday:", indi.Birthday, "is born after parents divorced: ",divorced_date )
            elif(indi_period.days>married_period.days and indi_period.days<divorced_period.days-270):
                print("Error Individual ID: US08 ",indiid,": birthday:", indi.Birthday, "is born after parents divorced: "\
                      ,divorced_date,"and also born before parents marriage : ",married_date )