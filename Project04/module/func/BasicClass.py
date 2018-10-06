import datetime

class Families:
    def __init__(self, ID):
        self.ID = ID
        self.Married = "NA"
        self.Divorced = "NA"
        self.HusbandID = "NA"
        self.HusbandName = "NA"
        self.WifeID = "NA"
        self.WifeName = "NA"
        self.Children = []


class Individuals: # 
    def __init__(self, ID):
        self.ID = ID
        self.Name = "NA"
        self.Gender = "NA"
        self.Birthday = "NA"
        self.Age = "NA"
        self.Alive = "NA"
        self.Death = "NA"
        self.Child = "None"
        self.Spouse = "NA"

    def isDateTimeForm(self, _str):
        if isinstance(_str, str) == True and len(_str.split('-')) == 3:
            year, month, day = _str.split('-')
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

    def str2DateTimeForm(self, _str):
        if self.isDateTimeForm(_str):
            return datetime.datetime.strptime(_str, '%Y-%m-%d')
        return None
    
    def getDT_Birthday(self):
        return self.str2DateTimeForm(self.Birthday)


def OrderById(inputLst):

    # input checking
    if len(inputLst) == 0 : return inputLst
    
    for item in inputLst:
        if isinstance(item, Individuals) == False and isinstance(item, Families) == False :
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


def getItemByID(inputLst, _id):

    # input checking
    if len(inputLst) == 0 : return inputLst
    
    for item in inputLst:
        if isinstance(item, Individuals) == False and isinstance(item, Families) == False :
            print("Unexpected List") 
            return inputLst
    
    orderedlst = []
    idDict = {}
    
    # making ID dict
    for idx,item in enumerate(inputLst):
        if _id == item.ID:
            return item

    return []



