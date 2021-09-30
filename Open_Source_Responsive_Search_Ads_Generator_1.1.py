#!/usr/bin/env python
# coding: utf-8

# In[13]:


"""RSA Generator 1.1 by Rares Finatan\nThis program outputs responsive search ads ready for Google Ads Editor or Microsoft Ads Editor upload.
Please follow the instructions outlined in the program to receive a CSV output of requested parameters.
Please note the variables provided in this file are simply for explanatory purposes and will require customization
to work for your intended project."""

import random
import pandas as pd

#define variables for randomization
adjectives = ['Affordable ', 'Cheap ', 'Low-Cost ', 'Budget ']
headline_phrases = ['Browse ', 'Book ', 'Find and Book ']
action_phrases = ['Book Now and Save on ', 'Discover ', 'Find Deals on ', 'Save Big on ']
semantic_variants = [" at Low Prices", " at Excellent Prices", " at Great Prices" ]

#request user input for topic
topic_phrases = input("What is the campaign or ad group about?\n\nFor best results, try listing at minimum 3 lexical permutations of what you are writing about for copy generation using \'&' as a delimiter.\nFor example: Flights&Hotels&Flight and Hotel Packages\n\nIf there are multiple items you would like to include in a single string, please pair them using the following syntax:\nFlights, Hotels, and More&Flight, Hotels, and Car Rentals\n\n")
topic_phrases = topic_phrases.split("&")
topic_phrases = list(topic_phrases)

print()

#request user input for branding
while True:
    branded_request = input("Is the campaign for a specific brand? Reply Y or N\n")
    if branded_request == "Y":
        branded_phrases = (input("Please specify the brand:")+ " ")
        break
    elif branded_request == " ":
        print("You must specify a response. Please revise your input:\n")
        continue
    elif branded_request == "N":
        branded_phrases = ""
        break

print()
    
#request user input for adjective
while True:
    additional_adjective = (input("Please specify one adjective to describe the product or service:\n") + " ")
#Default adjectives are the ones we've already specified in the adjectives variable above. 
#This additional_adjective variable is going to enable the user to add more variation that we may have omitted initially.
    if additional_adjective == " ":
        print("You must specify an adjective. Please revise your input:\n")
        continue
    else:
        break
adjectives.append(additional_adjective)
print(adjectives)

print()

#request user input for final destination URL
final_url = input("Please specify a final destination URL for this set of RSAs:")
print(final_url)

print()    

#create headlines
pd_headline = []
def headline():
    count = 0
    headline_set = set()
    for count in range (1,6):
        headline = (random.choice(headline_phrases) + branded_phrases + random.choice(topic_phrases))
        if len(headline) <= 30:
            headline_set.add(headline)
        count += 1
    for count in range (6,11):
        headline = (random.choice(adjectives) + random.choice(topic_phrases))
        if len(headline) <= 30:
            headline_set.add(headline)
        count += 1
    for count in range (11,16):
        headline = (random.choice(topic_phrases) + random.choice(semantic_variants))
        if len(headline) <= 30:
            headline_set.add(headline)
        count += 1
    for headline in headline_set:
        print(headline)
        pd_headline.append(headline)
        
headline()

print()

#create description lines
pd_description = []
def description():
    count = 0
    for count in range (0,5):
        description = (random.choice(action_phrases) + random.choice(adjectives) + branded_phrases + random.choice(topic_phrases) + random.choice(semantic_variants) + ".")
        if len(description) < 90:
            print(description)
            pd_description.append(description)
            
description()

#fill dataframe with inputs
df1 = pd.DataFrame()
for headline in pd_headline:
    df1.insert(0, "Headline", [headline], allow_duplicates = True)  
df1.columns = [f'{x} {i}' for i, x in enumerate(df1.columns, 1)]

df2 = pd.DataFrame()
for description in pd_description:
    df2.insert(0, "Description", [description], allow_duplicates = True)
df2.columns = [f'{x} {i}' for i, x in enumerate(df2.columns, 1)]

df3 = pd.DataFrame()
df3.insert(0, "Final URL", [final_url], allow_duplicates = True)

df1
df2
df3

df_export = pd.concat([df1, df2, df3], axis=1, join="inner")
df_export.to_csv('Automated_Responsive_Search_Ads.csv', index=False)


# In[ ]:





# In[ ]:




