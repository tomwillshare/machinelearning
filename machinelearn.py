#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:11:46 2017

@author: thomaswillshare
"""
from sklearn import tree
import sys, json

try:
    data = json.loads(sys.argv[1])
except:
    print "ERROR"
    sys.exit(1)

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [1, 1, 0, 0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150, 1]]))




# Generate some data to send to PHP
result = {'status': 'Yes!'}

# Send it to stdout (to PHP)
print json.dumps(result)
