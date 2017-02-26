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

enron_data = pickle.load(open("final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

print len(enron_data['HORTON STANLEY C'])

amount_poi=0
for person in enron_data: 
    if enron_data[person]['poi']==1: amount_poi+=1
print amount_poi

print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print enron_data['LAY KENNETH L']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

amount_folks_salary=0
for person in enron_data: 
    if enron_data[person]['salary']!='NaN': 
       amount_folks_salary+=1
print amount_folks_salary

amount_known_address=0
for person in enron_data: 
    if enron_data[person]['email_address']!='NaN':
       amount_known_address+=1
print amount_known_address

amount_total_payments_NaN=0
for person in enron_data: 
    if enron_data[person]['total_payments']=='NaN': 
       amount_total_payments_NaN+=1
print amount_total_payments_NaN / 146.000

amount_poi_total_payments_NaN=0
for person in enron_data: 
    if enron_data[person]['total_payments']=='NaN' and enron_data[person]['poi']==1: 
       amount_poi_total_payments_NaN += 1
print amount_poi_total_payments_NaN / 18.0

amount_total_payments_NaN=0
for person in enron_data: 
    if enron_data[person]['total_payments']=='NaN': 
       amount_total_payments_NaN+=1
print amount_total_payments_NaN