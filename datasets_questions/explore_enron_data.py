#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# find no of POI from json data
# <code>from pandas import DataFrame
# df = DataFrame(enron_data)
# len(df.ix['poi'].values[(df.ix['poi'].values == True)])
# shorter version: df.ix['poi'].value_counts()
# </code>

# count quantified salary
email_count = 0
for k in enron_data:
    if enron_data[k]['email_address'] != 'NaN':
        email_count += 1
print email_count

# count salary
salary_count = 0
for person in enron_data:
    if enron_data[person]['salary'] != 'NaN':
        salary_count += 1
print salary_count
