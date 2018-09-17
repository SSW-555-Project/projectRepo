
# coding: utf-8

# In[1]:


#Author: Po-Yu, Yang


# In[2]:


file_name_1="Project01(Po-Yu,Yang)"
file_name_2="proj02test"
#Valid Tag
valid_tags_set = set(['INDI','NAME','SEX','BIRT','DEAT','FAMC',             'FAMS','FAM','MARR','HUSB','WIFE','CHIL',             'DIV','DATE','HEAD','TRLR','NOTE'])


# In[3]:


def readAndPrint(filename):
    #read gedcom file
    filename=filename+".ged"
    input_ged = open(filename, "r") 
    saveFile="output_"+filename+".txt"
    writeFile = open(saveFile, "w")
    print ("Reading file : "+filename)
    writeFile.write("Reading file : "+filename+"\n")
    print ("File output : ")
    writeFile.write("File output : "+"\n")
    
    for each_input in input_ged:
        if len(each_input)>0 and each_input[:2]=="--":
            print(each_input)
            writeFile.write(each_input+"\n")
        if len(each_input)>0 and each_input[:2]!="--":
            each_input=each_input.rstrip("\n")
            flag="N"
            each_input_split=each_input.split()
            flag2=0

            print ("--> "+each_input)
            writeFile.write("--> "+each_input+"\n")
            if(len(each_input_split)>=1):
                word_count=2+len(each_input_split[1])+1
                
                if each_input_split[1] in valid_tags_set:
                    flag="Y"
                    flag2=1
                    if each_input_split[1] in set(['HEAD','TRLR','NOTE','INDI','FAM']):
                        if each_input_split[0] != 0:
                            flag2=3
                    elif each_input_split[1] == "DATE":
                        if each_input_split[0]!=2:
                            flag2=3
                if len(each_input_split)>2:
                    if each_input_split[2] in valid_tags_set:
                        flag="Y"
                        flag2=2
                    elif each_input_split[2]=="invalid":
                        flag2=3
                if flag2==1:   
                    print ("<-- "+each_input_split[0]+"|"+each_input_split[1]+"|"+flag+"|"+each_input[word_count:])
                    writeFile.write("<-- "+each_input_split[0]+"|"+each_input_split[1]+"|"+flag+"|"+each_input[word_count:]+"\n")
                elif flag2==2:   
                    print ("<-- "+each_input_split[0]+"|"+each_input_split[2]+"|"+flag+"|"+each_input_split[1])
                    writeFile.write("<-- "+each_input_split[0]+"|"+each_input_split[2]+"|"+flag+"|"+each_input_split[1]+"\n")
                else:
                    print ("<-- "+each_input_split[0]+"|"+each_input_split[1]+"|N|"+each_input[word_count:])
                    writeFile.write("<-- "+each_input_split[0]+"|"+each_input_split[1]+"|N|"+each_input[word_count:]+"\n")
        
    
    


# In[4]:


readAndPrint(file_name_1)


# In[5]:


readAndPrint(file_name_2)

