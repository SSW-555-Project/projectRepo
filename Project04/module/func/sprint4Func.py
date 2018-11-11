
# coding: utf-8

# In[ ]:


import datetime

#US_38_List upcoming birthdays
def US38_upcomingBirthdays(pp):
        currentYear = str(datetime.date.today().year)
        nextYear = str(datetime.date.today().year+1)
        if pp.Birthday[5:7] == '01':  #if the birthday is on January, it's possible that occurs 30 days later from December
            birthString = pp.Birthday.replace(pp.Birthday[:4], nextYear)
            birthday = datetime.datetime.strptime(birthString, "%Y-%m-%d").date()
        else:
            birthString = pp.Birthday.replace(pp.Birthday[:4], currentYear)
            birthday = datetime.datetime.strptime(birthString, "%Y-%m-%d").date()
        today = datetime.datetime.now().date()
        iterval = birthday - today
        if datetime.timedelta(days = 0) <= iterval <= datetime.timedelta(days=30):
            #print(pp.ID,pp.Name, birthday)
            return True
        
#US_39_List upcoming anniversaries
def US39_upcomingAnniversaries(fm):
    currentYear = str(datetime.date.today().year)
    nextYear = str(datetime.date.today().year+1)
    if fm.Married[5:7] == '01':
        marriedString = fm.Married.replace(fm.Married[:4], nextYear)
        marriedDay = datetime.datetime.strptime(marriedString, "%Y-%m-%d").date()
    else:
        marriedString = fm.Married.replace(fm.Married[:4], currentYear)
        marriedDay = datetime.datetime.strptime(marriedString, "%Y-%m-%d").date()
    today = datetime.datetime.now().date()
    iterval = marriedDay - today
    if datetime.timedelta(days = 0) <= iterval <= datetime.timedelta(days=30):
        #print(fm.ID, marriedDay)
        return True