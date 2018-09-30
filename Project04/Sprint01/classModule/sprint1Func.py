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

