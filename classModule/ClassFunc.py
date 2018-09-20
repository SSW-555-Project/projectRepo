from classModule import BasicClass
import inspect

def OrderById(inputLst):

    # input checking
    if len(inputLst) == 0 : return inputLst
    
    for item in inputLst:
        if isinstance(item, BasicClass.Individuals) == False and isinstance(item, BasicClass.Families) == False :
            print("Unexpected List") 
            return inputLst
    
    orderedlst = []
    idDict = {}
    
    # making ID dict
    for idx,item in enumerate(inputLst):
        if item.ID in idDict:
            print("Same ID exists")
            return inputLst
        else:
            idDict[item.ID] = idx
    
    # order by ID 
    sorted_by_value = sorted(idDict.items(), key=lambda kv: kv[0])

    # Re-making list
    for x in sorted_by_value:
        orderedlst.append(inputLst[idDict[x[0]]])

    return orderedlst

def DateBeforeCur(test_Year,test_Month,test_Day):
    if type(test_Year)!=int or type(test_Month)!=int or type(test_Day)!=int:
        print("Wrong data type for input")
        return False
    test_Date=datetime.date(test_Year,test_Month,test_Day)
    count=(test_Date-date.today())/datetime.timedelta(days=1)
    return count<0

#US01
def DateBeforeCur(test_Year,test_Month,test_Day):
    if type(test_Year)!=int or type(test_Month)!=int or type(test_Day)!=int:
        print("Wrong data type for input")
        return False
    test_Date=datetime.date(test_Year,test_Month,test_Day)
    count=(test_Date-date.today())/datetime.timedelta(days=1)
    return count<0

#US06
def ValidDivorcestr(indList,fList):
    for each in fList:
        if each.Divorced!="NA":
            for eachind in indList:
                if each.HusbandID==eachind.ID or each.WifeID=eachind.ID:
                    if eachind.Death!="NA":
                        death=(datetime.datetime.strptime(eachind.Death,"%Y-%m-%d")-datetime.datetime.strptime(\
                                                          each.Divorced,"%Y-%m-%d"))/datetime.timedelta(days=1)
                        if death<0:
                            print("No"+eachind.Id+": "+eachind.Name+" is dead before divorced. Please check again.")
                            return False
                    
    return True




