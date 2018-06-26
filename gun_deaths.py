
# coding: utf-8

# In[2]:


import csv
data = list(csv.reader(open('guns.csv')))
print(data[:5])


# In[3]:


headers = data[0]
data = data[1:]
print(headers)
print(data[:5])


# In[4]:


years = list(d[1] for d in data)
year_counts = {}
for year in years:
    if year not in year_counts:
        year_counts[year] = 1
    else: year_counts[year] += 1
year_counts


# # Gun Deaths by Year  
# The number of gun deaths per year doesn't seem to have changed much inbetween 2012 and 2014.

# In[5]:


import datetime 
dates = list(datetime.datetime(year = int(d[1]), month = int(d[2]), day = 1) for d in data)
dates[:5]


# In[6]:


date_counts = {}
for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    else: date_counts[date] += 1


# In[7]:


month_counts = {}
for date, count in date_counts.items():
    if date.strftime("%B") not in month_counts:
        month_counts[date.strftime('%B')] = date_counts[date]
    else: month_counts[date.strftime('%B')] += date_counts[date]
month_counts        


# # Gun Deaths by Month  
# The number of gun deaths was highest in the the month of July for both 2012 and 2013. If we add the total number of deaths that occured in each month over the three years, July has the highest occurance. This may be because American Independence day falls on the fourth of July and some of the shootings might have been politically motivated.

# In[8]:


month_homicide_count = {}
for i, date in enumerate(dates):
    if (data[i][3]=='Homicide' and 
        date.strftime("%B") not in month_homicide_count):
        month_homicide_count[date.strftime("%B")] = 1
    elif data[i][3]=='Homicide':
         month_homicide_count[date.strftime("%B")] += 1
month_homicide_count        


# # Homicide by Month  
# When we look at the number of homicides per a month over the four years, we see that July still has the highest tally. The difference, however, is not remarkable.  This would indicate that there are a fair number of suicides in July as well.  This could possibly be as a result of people feeling lonely during Idependance celebrations or over the summer break. 

# In[9]:


sex_counts = {}
sex_counts["Male"] = 0
sex_counts["Female"] = 0
for d in data:
    if d[5]=='M': sex_counts["Male"] += 1
    elif d[5]=='F': sex_counts["Female"] += 1
sex_counts


# # Gun deaths by Gender  
# Surprisingly most of the gun deaths victims in the US are male. Although women are often the victims of violence because they are seen as soft targets, men are more likely to be involve in gang activity. Studies have also shown that men who commit suicide are more likely to use firearms while women generally prefer less violent means. 

# In[10]:


race_counts = {}
for d in data:
    if d[7] not in race_counts: race_counts[d[7]] = 1
    else: race_counts[d[7]] += 1
race_counts


# # Gun Deaths by Race  
# The largest number of gun death victims in the US are White, with Black victims coming in second place.  Because the largest Demographic group is White and the second largest is Black, this doesn't indicate that a particular group is being targeted. 

# In[11]:


census = list(csv.reader(open("census.csv")))
print(census)


# In[12]:


mapping = {}
mapping['Asian/Pacific Islander'] = int(census[1][14]) + int(census[1][15])
mapping['Black'] = int(census[1][12])
mapping['Native American/Native Alaskan'] = int(census[1][13])
mapping['Hispanic'] = int(census[1][11])
mapping['White'] = int(census[1][10])
race_per_hundredk = {}
for race in race_counts:
    race_per_hundredk[race] = race_counts[race]*100000/mapping[race]
race_per_hundredk


# # Gun Deaths per 100 000 by Race  
# It is interesting that when we take the population size into account, Blacks are now most likely to be victims of gun death, with Whites second, then native American and lastly Hispanic.  This may be related to poverty and living in crime ridden areas.

# In[13]:


intents = list(d[3] for d in data)
races = list(d[7] for d in data)
homicide_race_counts = {}
for i, race in enumerate(races):
    if intents[i]=="Homicide" and race not in homicide_race_counts:
        homicide_race_counts[race] = 1
    elif intents[i]=="Homicide": homicide_race_counts[race] += 1
for race, count in homicide_race_counts.items():
    homicide_race_counts[race] = count*100000/mapping[race]
homicide_race_counts


# # Homicide per 100 000 by Race  
# When we filter the gun deaths to show the number of homicides only, per 100k by race, we see a very different result.  Black victims are still the majority, but now we see Hispanics and Whites having switched places.  This may be because many of the White gun deaths are suicides.  The Hispanics, however, many of whom are immigrants, may be more likely to get involved in gang activity. 

# In[14]:


gender_suicide = {}
gender_suicide['Male'] = 0
gender_suicide['Female'] = 0
for d in data:
    if d[3]=='Suicide' and d[5]=='M':
        gender_suicide['Male'] += 1
    elif d[3]=='Suicide' and d[5]=='F':
        gender_suicide['Female'] += 1
gender_suicide


# # Gender Suicide  
# Here we can clearly see that men are far more likely to use a firearm to commit suicide, while women would usually choose a less violent means.  Of the suicide victims, only about a seventh of them were female. 

# In[15]:


gender_accident = {}
gender_accident['Male'] = 0
gender_accident['Female'] = 0
for d in data:
    if d[3]=='Accidental' and d[5]=='M':
        gender_accident['Male'] += 1
    elif d[3]=='Accidental' and d[5]=='F':
        gender_accident['Female'] += 1
gender_accident


# # Gender Accident  
# Women are definately the more cautious of the genders, with only about an eighth of accidental gun deaths vitims being female. 

# In[16]:


from collections import OrderedDict
educ_counts = OrderedDict()
for d in data:
    if d[10]=='1' and 'No High School Certificate' not in educ_counts:
        educ_counts['No High School Certificate'] = 1
    elif d[10]=='1':
        educ_counts['No High School Certificate'] += 1
    elif d[10]=='2' and 'High School Cerificate' not in educ_counts:
        educ_counts['High School Cerificate'] = 1
    elif d[10]=='2':
        educ_counts['High School Cerificate'] += 1
    elif d[10]=='3' and 'Some College' not in educ_counts:
        educ_counts['Some College'] = 1
    elif d[10]=='3':
        educ_counts['Some College'] += 1
    elif d[10]=='4' and 'College Graduate' not in educ_counts:
        educ_counts['College Graduate'] = 1
    elif d[10]=='4':
        educ_counts['College Graduate'] += 1
educ_counts


# # Gun Deaths by Education  
# Most of the gun death victims have a High school certificate.  This may be because there are few Americans who don't have one. When we look at the gun death victims who have attended college and those who have graduated from college we see that there are progressively fewer of them.  Lets see what happens when we look at gun deaths per 100k of individuals in each group. 

# In[18]:


from collections import OrderedDict
educ_suicide = OrderedDict()
for d in data:
    if d[3]=='Suicide':
        if d[10]=='1' and 'No High School Certificate' not in educ_suicide:
            educ_suicide['No High School Certificate'] = 1
        elif d[10]=='1':
            educ_suicide['No High School Certificate'] += 1
        elif d[10]=='2' and 'High School Cerificate' not in educ_suicide:
            educ_suicide['High School Cerificate'] = 1
        elif d[10]=='2':
            educ_suicide['High School Cerificate'] += 1
        elif d[10]=='3' and 'Some College' not in educ_suicide:
            educ_suicide['Some College'] = 1
        elif d[10]=='3':
            educ_suicide['Some College'] += 1
        elif d[10]=='4' and 'College Graduate' not in educ_suicide:
            educ_suicide['College Graduate'] = 1
        elif d[10]=='4':
            educ_suicide['College Graduate'] += 1
for x in educ_suicide:
    educ_suicide[x] = educ_suicide[x]*100/educ_counts[x]
educ_suicide


# # Suicide Rate (%) by Education  
# When we examine the percentage of gun deaths that were suicide for each group, we find that the higher the level of education, the larger the percentage of gun deaths that can be attributed to suicide. Of those who have graduated from college, 86% of the gun deaths were listed as suicide, while of those who have no high school certificate, only 43%  of the gun deaths were listed as suicide.  
