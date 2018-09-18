
# coding: utf-8

# In[17]:


from classModule.otcls import * 
import time
import datetime
from datetime import date
import prettytable as pt

valid_tags = {0:["INDI","FAM","HEAD","TRLR","NOTE"],            1:["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV"]         ,2:"DATE"}
file_name_1="My-Family-17-Sep-2018-358"
file_name_2="courseExample"
individualList=[]
familyList=[]
def monthToNum(shortMonth):
    return{
            'JAN' : 1,
            'FEB' : 2,
            'MAR' : 3,
            'APR' : 4,
            'MAY' : 5,
            'JUN' : 6,
            'JUL' : 7,
            'AUG' : 8,
            'SEP' : 9, 
            'OCT' : 10,
            'NOV' : 11,
            'DEC' : 12
    }[shortMonth]

def readAndSaveToList(filename,List,List2):
    #read gedcom file
    filename=filename+".ged"
    input_ged = open(filename, "r") 
   # saveFile="output_"+filename+".txt"
   # writeFile = open(saveFile, "w")
    #set flags
    flag_Birth=False
    flag_Death=False
    flag_Married=False
    flag_Divorced=False
    #read each line to input

    for each_input in input_ged:
        # Ensure line is not empty or comments
        if len(each_input)>0 and each_input[:2]!="--":
            each_input=each_input.rstrip("\n")
          #  print(each_input)
            each_input_split=each_input.split()
            # Ensure there're level and tag
            if len(each_input_split)>=2:
                level,tag=int(each_input_split[0]),each_input_split[1]
                # Ensure input is valid
                word_count=2+len(tag)+1
                # Ensure there's desc to process
                if len(each_input_split)>=3:
                    desc=each_input_split[2]
                    # Detect New Individual and create new class
                    if desc=="INDI":
                        ID=tag[0:3]
                        p1=Individuals(ID)
                        List.append(p1)
                    # Detect New Family and create new class
                    if desc=="FAM":
                        ID=tag
                        f1=Families(ID)
                        List2.append(f1)    
                    if tag=="SEX":
                        SEX=desc  
                        p1.Gender=SEX    
                    if tag=="NAME":
                        NAME=each_input[word_count:].strip()
                        p1.Name=NAME
                    if flag_Birth==True and tag=="DATE":
                        B_DAY=int(desc)
                        B_MONTH=int(monthToNum(each_input_split[3]))
                        B_YEAR=int(each_input_split[4])
                        
                        Birthday=datetime.date(B_YEAR,B_MONTH,B_DAY)
                        p1.Age=int ((date.today()-Birthday)/datetime.timedelta (days=1)/365)
                        p1.Birthday=str(Birthday)
                        flag_Birth=False   
                    if flag_Death==True and tag=="DATE":
                        D_DAY=int(desc)
                        D_MONTH=int(monthToNum(each_input_split[3]))
                        D_YEAR=int(each_input_split[4])
                        
                        Death=datetime.date(D_YEAR,D_MONTH,D_DAY)
                        p1.Age=int((Death-Birthday)/datetime.timedelta (days=1)/365)
                        p1.Death=str(Death)
                        flag_Death=False
                    if flag_Married==True and tag=="DATE":
                        M_DAY=int(desc)
                        M_MONTH=int(monthToNum(each_input_split[3]))
                        M_YEAR=int(each_input_split[4]) 
                        MarriedDay=datetime.date(M_YEAR,M_MONTH,M_DAY)
                        f1.Married=str(MarriedDay)
                    if flag_Divorced==True and tag=="DATE":
                        D_DAY=int(desc)
                        D_MONTH=int(monthToNum(each_input_split[3]))
                        D_YEAR=int(each_input_split[4]) 
                        DivorcedDay=datetime.date(B_YEAR,B_MONTH,B_DAY)
                        f1.Divorced=str(DivorcedDay)
                    if tag=="FAMS":
                        Spouse=desc
                        p1.Spouse=Spouse
                    if tag=="FAMC":
                        Child=desc
                        p1.Child=Child
                    if tag=="HUSB":
                        Husband=desc
                        f1.HusbandID=Husband
                        for each in List:
                            if each.ID==f1.HusbandID: 
                                f1.HusbandName=each.Name      
                    if tag=="WIFE":
                        Wife=desc
                        f1.WifeID=Wife
                        for each in List:
                            if each.ID==f1.WifeID: 
                                f1.WifeName=each.Name
                    if tag=="CHIL":
                        Children=desc
                        f1.Children.append(Children)
                elif len(each_input_split)==2:
                    if tag=="BIRT":
                        flag_Birth=True
                        p1.Alive="True"
                    if tag=="DEAT":
                        flag_Death=True
                        p1.Alive="False"
                    if tag=="MARR":
                        flag_Married=True
                    if tag=="DIV":
                        flag_Divorced=True
                        


# In[18]:


readAndSaveToList(file_name_2,individualList,familyList)


# In[19]:


len(individualList)

for each in individualList:
   # print(each.ID+each.Name+"\t"+str(each.Age)+"\t"+each.Birthday+"\t"+each.Death+each.Alive)
    print(each.Spouse)


# In[20]:


for each in familyList:
    print(each.Children)


# In[22]:


tb=pt.PrettyTable()
tb.field_names=["ID","Name","Gender","Birthday","Age","Alive","Death"                ,"Child","Spouse"]
for each in individualList:
    tb.add_row([each.ID,each.Name,each.Gender,each.Birthday,each.Age,              each.Alive,each.Death,each.Child,each.Spouse])
print(tb)


# In[23]:


tb2=pt.PrettyTable()
tb2.field_names=["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name"                ,"Children"]
for each in familyList:
    tb2.add_row([each.ID,each.Married,each.Divorced,each.HusbandID,each.HusbandName,              each.WifeID,each.WifeName,each.Children])
print(tb2)


# In[26]:


writefile = open("output.txt","w") 
writefile.write("Individuals") 
writefile.write(tb.get_string()) 
writefile.write("\n") 
writefile.write("Families") 
writefile.write(tb2.get_string()) 
writefile.close()

