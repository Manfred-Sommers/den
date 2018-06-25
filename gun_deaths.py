
# coding: utf-8

# # US Births  
# ## CHRISTMAS DAY SEEMS LIKE THE LEAST POPULAR DAY TO GIVE BIRTH  
# Columns from Left to right:  
# >Year  
# Month  
# Day of Month  
# Day of Week (1 = Monday)  
# Number of Births

# In[59]:


def read_csv(file):
    string_list = open(file,"r").read().split("\n")
    final_list =[]
    for s in string_list[1:]:
        int_fields =[]
        string_fields = s.split(",")
        for x in string_fields:
            int_fields.append(int(x))
        final_list.append(int_fields)
    return final_list


# In[60]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
for i in range(10):
    print(cdc_list[i])


# In[61]:


ssa_list = read_csv("US_births_2000-2014_SSA.csv")
ssa_list


# In[62]:


def calc_count(data,column):
    births_per_column = {}
    for d in data:
        if d[column] in births_per_column.keys():
            births_per_column[d[column]] += d[4]
        else: births_per_column[d[column]] = d[4]
    return births_per_column


# In[63]:


cdc_year_births = calc_count(cdc_list, 0)
cdc_year_births


# In[64]:


ssa_year_births = calc_count(ssa_list, 0)
ssa_year_births


# ## Births Per Year  
# 1997 seems to have been the year with the lowest number of births while 2007 seems to have been the year with the highest number of births.

# In[90]:


cdc_month_births = calc_count(cdc_list,1)
cdc_month_births


# In[89]:


ssa_month_births = calc_count(ssa_list,1)
ssa_month_births


# ## Births per Month  
# Both the cdc, as well as the ssa data sets indicate that August was the month with the highest number of births.  The cdc as well as the ssa data sets also both concurr on the month with the lowest number of births, namely February.

# In[91]:


cdc_dom_births = calc_count(cdc_list,2)
cdc_dom_births


# In[93]:


ssa_dom_births = calc_count(ssa_list,2)
ssa_dom_births


# ## Births per Day of Month  
# Both data sets obviously show that the 31st is the day of the month with the lowest birth rate as it has the lowest frequency, while they both indicate that the 18th and the 20th respectively have the highest number of births.

# In[95]:


cdc_dow_births = calc_count(cdc_list, 3)
cdc_dow_births


# In[94]:


ssa_dow_births = calc_count(ssa_list, 3)
ssa_dow_births


# ## Births per Day of Week  
# Both data sets indicate that there is a higher number of births during the working days and a lower number of births over the weekend.  Both sets show that Tuesday is the day with the highest number of births, while Sunday is the day with the lowest number of births.
# 

# In[68]:


def min_births(data):
    min_list = data[0]
    for d in data:
        if d[4] < min_list[4]: min_list = d
    return min_list


# In[96]:


cdc_min = min_births(cdc_list)
print(cdc_min)
ssa_min = min_births(ssa_list)
print(ssa_min)


# In[70]:


def max_births(data):
    max_list = data[0]
    for d in data:
        if d[4] > max_list[4]: max_list = d
    return max_list


# In[97]:


cdc_max = max_births(cdc_list)
print(cdc_max)
ssa_max = max_births(ssa_list)
print(ssa_max)


# In[72]:


def min_criteria(data, column, value):
    possible = []
    for d in data:
        if d[column] == value:
            possible.append(d)
    min_list = possible[0]
    for p in possible:
        if p[4] < min_list[4]: min_list = p
    return min_list
        


# In[87]:


for i in range (1994, 2004):
    cdc_min = min_criteria(cdc_list, 0, i)
    print(cdc_min)


# In[88]:


for i in range(2000,2015):
    ssa_min = min_criteria(ssa_list, 0, i)
    print(ssa_min)


# ##  Date of Minimum Births per Year  
# Both data sets indicate that the Christmas day is the usually the day of the year with the lowest number of biths.  Inbetween 1994 and 2014 there were only two years when this wasn't the case.  In 1995 the day with the lowest number of births was Christmas eve and in 2013 it was the 5th of May.  
# (note in the years 2000-2003 where the data sets overlap there was a difference of between 100 and 200 births between the cdc and ssa sets)   

# In[100]:


def max_criteria(data, column, value):
    possible = []
    for d in data:
        if d[column] == value:
            possible.append(d)
    max_list = possible[0]
    for p in possible:
        if p[4] > max_list[4]: max_list = p
    return max_list


# In[101]:


for i in range (1994, 2004):
    cdc_max = max_criteria(cdc_list, 0, i)
    print(cdc_max)


# In[102]:


for i in range (2000, 2015):
    ssa_max = max_criteria(ssa_list, 0, i)
    print(ssa_max)


# ## Date of Maximum Births per Year  
# While there doesn't seem to as much of a distinct pattern when we examine the date of the maximum number of births per a year, there are a couple of inferences we can draw.  With the exception of 1994 and 1996 all the other years had a date inbetween September and December for the highest number of births, with the 30th of December being the mode.  This makes our previous discovery that the day of the year with the least number of births is usually Christmas day even more astounding.
