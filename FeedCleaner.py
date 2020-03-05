filename=input("Please enter the file name..  ")
filepath = "C:/Users/qihus/Desktop/{}.csv".format(filename)  #just change the path

import pandas as pd
import spacy
import en_core_web_lg
nlp = en_core_web_lg.load()

data = pd.read_csv(filepath)#file name ; incl directory

data.drop_duplicates(subset ="TITLE", 
                     keep = 'first', inplace = True) 

data.drop_duplicates(subset ="LINK", 
                     keep = 'first', inplace = True) 

data.drop_duplicates(subset =["ROUND COMPANY NAME","ROUND AMOUNT (M)","ROUND CURRENCY"], 
                     keep = 'first', inplace = True) 




print(len(data.index)) ## check current count  after first filter




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

print(len(data.index)) 

data.to_csv("out_{}.csv".format(filename))# output file name 