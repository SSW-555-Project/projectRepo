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



