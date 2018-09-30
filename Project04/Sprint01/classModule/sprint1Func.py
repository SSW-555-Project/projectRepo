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