#!/usr/bin/env python
# coding: utf-8

# In[1]:


# take first element for sort
def takeFirst(elem):
    return elem[0]

import re

def create_iob(line, labels):
    
    
    text_line = list(line["text"])
    text_list = line["text"].split(" ")
    final_list = []
    period_list = []
    
    # this is for copying over the periods after the 
    # entire transform is over
    for t in text_list:
        
        #First mark everything O and push it into a list
        period_text = t.strip(",/\;-")
        period_list.append(period_text)

    for t in text_list:
        
        #First mark everything O and push it into a list
        annotated_text = t.strip(",./\;-")+" O"
        final_list.append(annotated_text)
        
    # make sure the labels are sorted by index position
    labels.sort(key=takeFirst)

    #loop through the labels to check char positions where labels exist
    for label in labels:
        start = label[0]
        end = label[1]
        iob_term = label[2]
        entity_chars = text_line[start:end]

        entity_list = ''.join(entity_chars).split(" ")

        if len(entity_list) > 1:
            if entity_list[0] != '':
                #print(entity_list[0], "B-", label[2])

                compare_string = entity_list[0]+" O"
                annotated_text = entity_list[0]+" B-"+iob_term

                try:
                    pos = final_list.index(compare_string)
                    final_list[pos] = annotated_text
                except:
                    pass

            for e in entity_list[1:]:

                #print(e, "I-",label[2])
                compare_string = e+" O"
                annotated_text = e+" I-"+iob_term

                try:
                    pos = final_list.index(compare_string)
                    final_list[pos] = annotated_text
                except:
                    pass
        else:
            if entity_list[0] != '':
                #print(entity_list[0], "B-",iob_term)
                compare_string = entity_list[0]+" O"
                annotated_text = entity_list[0]+" B-"+iob_term

                try:
                    pos = final_list.index(compare_string)
                    final_list[pos] = annotated_text
                except:
                    pass
    
    # before we send the final list back we need to 
    # replace the periods that got removed
    
    print(len(period_list))
    print(len(final_list))
    i = 0
    while i < len(final_list):
        #if there is a period in the period list, then 
        #insert it into the final list
        print("*** ", period_list[i])
       
        if (re.match(r'[a-z]*[=?,;]*\. *', period_list[i])) is not None:
            print("matched ", period_list[i], final_list[i])
            split_final_list_item = final_list[i].split(" ")
            with_period_final_list_item = split_final_list_item[0]+"."+" "+split_final_list_item[1]
            print(">>", with_period_final_list_item)
            final_list[i] = with_period_final_list_item
        i += 1
         
         
    return(final_list)


# In[2]:


import json


json_file = open("/Users/titashneogi/workspace/flair-experiments/jobsdata/indeed_tagged.json", "r")
#conll_file = open("/Users/titashneogi/workspace/flair-experiments/jobsdata/indeed_tagged.txt","w+")

conll_file = open("/Users/titashneogi/workspace/NLP/NER/Spacy NER/indeed_tagged.txt","w+")

for eachline in json_file:
    line = json.loads(eachline)
    split_line = line["text"].split(" ")
    
    if line["labels"] != None:
        labels = line["labels"]
        
        iob_list = create_iob(line, labels)
        
        if iob_list != "":
            for f in iob_list:
                #strip starting space and then check if there is 
                #still space so that indicates a valid tagging
                cleaned_f = f.strip()
               
                if (len(cleaned_f.split()) == 2):
                    conll_file.write(cleaned_f)
                    #comment this second newline fi not for spacy
                    #conll_file.write("\n") 
                    conll_file.write("\n")   
    else:
        continue

conll_file.close()


# In[ ]:





# In[ ]:


# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("/Users/titashneogi/workspace/NLP/NER/data/flair/eng_turk/EWNERTC.csv")

# Preview the first 5 lines of the loaded data 
data.head()


# In[ ]:


data.head(n=100)


# In[ ]:


df = pd.DataFrame(data)


# In[ ]:


print(df)


# In[ ]:


newDf = df[['Sentences', 'Tags']]


# In[ ]:


newDf.to_csv('/Users/titashneogi/workspace/NLP/NER/data/flair/ewnet.tsv', index=False, sep='\t')


# In[ ]:




