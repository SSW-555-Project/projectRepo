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



