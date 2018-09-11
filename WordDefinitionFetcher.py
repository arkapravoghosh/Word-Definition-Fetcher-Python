# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 22:19:48 2018

@author: Dr. Amal K Ghosh
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDefinition(word):
    word = word.lower()
    if word in data: 
        return data[word]
    if word.title() in data:
        return data[word.title()]
    if word.upper() in data:
        return data[word.upper()]
    for i in get_close_matches(word, data.keys(), 5):
        ch = input("Did you mean %s instead(Y/N)? " %i)
        if(ch != "Y" and ch != "N"):
          return ["We didn't understand your entry."]  
        if(ch == "Y"):
            return data[i]
    return ["Word not found!! Please check again."]
    
word = input("Enter a word: ")

[print(i) for i in getDefinition(word)]