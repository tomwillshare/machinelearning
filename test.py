#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 19:37:55 2018
@author: dipu
"""
#!/anaconda3/bin/python
import json
import requests
import sys
from sklearn import tree
import cgi

'''
get the column count of the vector
i.e. number of features
'''
def count_column(split_value):
    column_count=-1
    for row in split_value:
        if(row[1] != 'yes' and row[1]!='no'):
            column_count += 1
        else:
            column_count += 1
            break
    return column_count

'''
append zeros to each rows  whose length is less than column_count or which has less feature than required
to make it a (n) column vector
'''
def append_zeros(final_value_list,column_count):

    for i in range(len(final_value_list)-1):
        while(len(final_value_list[i])<column_count):
            final_value_list[i].append(0)

    return final_value_list

'''
get the final matrix value to be put into the classifier
'''
def get_matrix(value_list,column_count):
    final_value_list=[]
    labels=[]
    list_iterator = 0
    while(list_iterator < len(value_list)):
        value_row = []
        for j in range(column_count+1):
            if(value_list[list_iterator].lower() == 'yes'):
                labels.append(0)
            elif(value_list[list_iterator].lower() == 'no'):
                labels.append(1)
            elif(value_list[list_iterator] == ''):
                pass
            else:
                value_row.append(value_list[list_iterator])
            list_iterator += 1
            if(list_iterator >= len(value_list)):
                break
        final_value_list.append(value_row)
        if(list_iterator >= len(value_list)):
            break
    final_value_list=append_zeros(final_value_list,column_count)
    testdata=[]
    testdata.append(final_value_list[-1])
    features = final_value_list[:-1]
    return features, labels, testdata

'''
prepare the data for the classifier
and divides the data into trainning and testing set
'''
def prepare_data(pythondata):
    split_value_list = [(lambda x: x.split(":"))(x) for x in pythondata]
    split_value_list = split_value_list[1:]
    column_count= count_column(split_value_list)
    value_list = [(lambda x: x[1])(x) for x in split_value_list]
    features, labels, testdata=get_matrix(value_list,column_count)
    return features, labels, testdata


if __name__ == "__main__":
    '''imports from php'''
    who = sys.argv

    '''turns json data into string'''
    json_string = json.dumps(who)
    pythondata = json.loads(json_string)

    features, labels, testdata = prepare_data(pythondata)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    answer = clf.predict(testdata)

    if answer == 0:
        print('yes')
    else:
        print('no')
