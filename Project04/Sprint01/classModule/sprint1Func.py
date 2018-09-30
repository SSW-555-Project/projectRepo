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
            print("ERROR: US01: Date "+str(day)+" is not before current time.")
    return 


def isDivorceBeforeDeath(divorceday, deathday):
    # US06 Check whether divorce date is before death date or not
    # Assume temporarily that this function will be call twice. (husband and wife)

    if isinstance(divorceday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(divorceday) == False :
            return False
        divorceday = datetime.datetime.strptime(divorceday, '%Y-%m-%d')
    
    if isinstance(deathday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isDataFormat(deathday) == False :
            return False
        deathday = datetime.datetime.strptime(deathday, '%Y-%m-%d')

    if(divorceday - deathday).total_seconds() > 0 :
        print("ERROR: FAMILY: US06 : Divorced on "+str(divorceday)+" after death on "+str(deathday))
    return

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
