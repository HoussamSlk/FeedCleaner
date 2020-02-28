#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import spacy
import en_core_web_lg
nlp = en_core_web_lg.load()

data = pd.read_excel("")#file name ; incl directory

data.drop_duplicates(subset ="TITLE", 
                     keep = 'first', inplace = True) 

data.drop_duplicates(subset ="LINK", 
                     keep = 'first', inplace = True) 

data.drop_duplicates(subset =["ROUND COMPANY NAME","ROUND AMOUNT (M)","ROUND CURRENCY"], 
                     keep = 'first', inplace = True) 


# In[2]:


len(data.index) ## check current count  after first filter


# In[3]:


for row in data.iterrows():  ## checks similarity of contents
    x1 = nlp(str(row[1]['SUMMARY']))
    x2 = nlp(str(row[1]['CONTENT']))
    for sec_row in data.iterrows():
        y1 = nlp(str(sec_row[1]['SUMMARY']))
        y2 = nlp(str(sec_row[1]['CONTENT']))
        yid = sec_row[1]['ID']
        if (row[1]['ID'] == sec_row[1]['ID']) :
            continue
        if(x1.similarity(y1)>=0.940950 and x2.similarity(y2)>=0.940950):
            data = data[data.ID != yid]


# In[4]:


len(data.index)


# In[6]:


len(data.index)


# In[7]:


data.to_excel(".xlsx")# output file name 

