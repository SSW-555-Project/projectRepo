import datetime


def isBirthBeforeDeath(birthday, deathday):
    # US03 Birth should occur before death of an individual

    if isinstance(birthday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        return False
    
    if isinstance(deathday, datetime.date) != True:
        #msg = "The type of deathday is not datetime"
        return False

    if(deathday - birthday).total_seconds() > 0 :
        return True
    else:
        return False

def isMarriageBeforeDeath(marriageday, deathday):
    # US05 Marriage should occur before death of either spouse
    # Assume temporarily that this function will be call twice. (husband and wife)

    if isinstance(marriageday, datetime.date) != True:
        #msg = "The type of marriageday is not datetime"
        return False
    
    if isinstance(deathday, datetime.date) != True:
        #msg = "The type of deathday is not datetime"
        return False

    if(deathday - marriageday).total_seconds() > 0 :
        return True
    else:
        return False

    
    
def isDateBeforeCur(day):
    # US01 Every dates should be earlier before current date
    if isinstance(day, str) != True:
        print("msg: The type of "+day+" is not str.")  
        return
    date=datetime.datetime.strptime(day, '%Y-%m-%d')
    if (date-datetime.datetime.now()).days>0:
        print("ERROR: US01: Date is not before current time.")
    return 

def isValidDivorce(divorceday, deathday):
    # US06 Check whether divorce date is before death date or not
    if isinstance(divorceday, str) != True:
        print("msg = The type of "+divorceday+" is not str")
        return 
    if isinstance(deathday, str) != True:
        print("msg = The type of "+deathday+" is not str")
        return  
    divorce=datetime.datetime.strptime(divorceday, '%Y-%m-%d')
    death=datetime.datetime.strptime(deathday, '%Y-%m-%d')
    if(divorce - death).days > 0 :
        print("ERROR: FAMILY: US06 : Divorced on "+divorceday+" after death on "+deathday)
    return 