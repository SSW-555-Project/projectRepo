import datetime

def isStrDataFormat(date):
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

def checkStrDateFormat(inlst):
    for day in inlst:
        if isStrDataFormat(day) == False :
            return False
    return True

def checkDateFormat(day1, day2):
    lst = [day1, day2]
    result = []
    flag = True
    for day in lst:
        if isinstance(day, datetime.date) == False :
            if isStrDataFormat(day):
                result.append(datetime.datetime.strptime(day, '%Y-%m-%d'))
            else:
                flag = False
        else:
            result.append(day)
            
    if len(result) != 2:
        return 0, 0 , False
    
    return result[0], result[1], flag

def ispPositiveTimeDuration(day1, day2):

    if(day1 - day2).total_seconds() > 0 :
        return True
    else:
        return False


def isBirthBeforeDeath(birthday, deathday):
    # US03 Birth should occur before death of an individual
    if deathday == 'NA':
        return True  

    deathday, birthday, flag = checkDateFormat(deathday, birthday)
    
    if flag == False:
        return False

    return ispPositiveTimeDuration(deathday, birthday)


def isMarriageBeforeDeath(marriageday, deathday):
    # US05 Marriage should occur before death of either spouse
    # Assume temporarily that this function will be call twice. (husband and wife)
    if deathday == 'NA':
        return True  

    deathday, marriageday, flag = checkDateFormat(deathday, marriageday)
    
    if flag == False:
        return False

    return ispPositiveTimeDuration(deathday, marriageday)

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
        if isStrDataFormat(divorceday) == False :
            return True
        divorceday = datetime.datetime.strptime(divorceday, '%Y-%m-%d')
    
    if isinstance(deathday, datetime.date) != True:
        #msg = "The type of birthday is not datetime"
        if isStrDataFormat(deathday) == False :
            return True
    
        deathday = datetime.datetime.strptime(deathday, '%Y-%m-%d')

    if(divorceday - deathday).total_seconds() > 0 :
        return False
    return True

def isbirthBFmarried(fmID, fmDay,iBirth):
    if fmDay != 'NA': 
        birth = datetime.datetime.strptime(iBirth, "%Y-%m-%d").date()
        marrDay = datetime.datetime.strptime(fmDay, "%Y-%m-%d").date()
        ID = fmID

        if (birth - marrDay).total_seconds() > 0:
            return False
        else:
            #print(f"FAMILY: US02: {ID} married day '{marrDay}' is valid")
            return True
    else:
        print(f"No Married date provided!")
        return


def isAgeLThen150(indi):
    if indi != None: 
        ID = indi.ID
        Age = indi.Age
        if Age > 150:
            # raise ValueError('The age is over 150!')
            return False
        else:
        #print(f"INDIVIDUAL: US07 {ID}'s age '{Age}' is less than 150 ")
            return Age < 150
    else:
        print("No individual can be tested")
        return
    
def US04(famID,Date_married,Date_divorced):
    from datetime import datetime
    if(Date_married!="NA" and Date_divorced!="NA"):
        result=datetime.strptime(Date_divorced, "%Y-%m-%d")-datetime.strptime(Date_married, "%Y-%m-%d")
        #print(Date_divorced,Date_married)
        #print(result.days)
        if(result.days<0):
            #print("==Error Family: US04 ",famID," : Marriage",Date_married, "after divorce",Date_divorced )
            return False
        else:
            #print("==Family: US04 ",famID," : Marriage",Date_married, "before divorce",Date_divorced, "is valid" )
            return True
    else:
        return True
            
            
def US08(iList,famID,ID,married_date,divorced_date,famChild):
    from datetime import datetime
    
    if(married_date!="NA" and divorced_date!="NA"):
        for indi in iList:
            if (indi.ID in famChild):
                abc=""
                indiid=indi.ID
                married_period= datetime.now()- datetime.strptime(married_date, "%Y-%m-%d")
                indi_period= datetime.now()- datetime.strptime(indi.Birthday, "%Y-%m-%d")
                divorced_period= datetime.now()- datetime.strptime(divorced_date, "%Y-%m-%d")
                #print("Take a look",married_period.days, indi_period.days, divorced_period.days)
                if(indi_period.days>married_period.days and indi_period.days>=divorced_period.days-270):
                    abc="ERROR: INDIVIDUAL: US08: {0}: {1} Birth before parents marriage "\
                    "{2}".format(indiid,indi.Birthday,married_date)
                    return abc
                elif(indi_period.days<married_period.days and indi_period.days<divorced_period.days-270):
                    abc="ERROR: INDIVIDUAL: US08: {0}: {1} " \
                    "Birth after parents divorced {2}".format(indiid,indi.Birthday,divorced_date)
                    return abc
                elif(indi_period.days>married_period.days and indi_period.days<divorced_period.days-270):
                    abc="ERROR: INDIVIDUAL: US08: {0}: {1} "\
                    "Birth after parents divorced {2} and before parents marriage "\
                    "{3}".format(indiid,indi.Birthday,divorced_date,married_date)
                    return abc