# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:21:47 2021

@author: GrandLoup
"""

import re # regular expressions library

# will check if tiger is in the start
string1 = "Tiger is the national animal of India."
result = re.match("Tiger", string1).group(0) # match only searches at the start
print(result)
print(re.search("animal", string1).group(0)) # use group(0) to return object content

string2 = "John 34-3456 12-05-2007, Loubens 56-4532 01-04-1991, Arya 67-8945 12-01-2009"
pattern = r'\d{2}-\d{2}-\d{4}'
result2 = re.findall(pattern, string2)
print(result2)

result22 = re.finditer(pattern, string2) # to find index of match
for word in result22: # iteratively print out indexes for multiple matches
    print(word)
    
for word in result22: # iteratively print out indexes for multiple matches
    print(word.start())
    


result3 = re.split(r'[,]', string2)
print(result3)

result4 = re.sub('Arya', 'Daenarys', string2)
print(result4)



########## 
string3 = "Ron was born on 12-09-1992, and he was admitted to school on 15-12-1999."
pattern = r'\d{2}-\d{2}-\d{4}'
result5 = re.findall(pattern, string3)
print(result5)
result6 = re.sub(pattern, "a Monday", string3)
print(result6)


email = "my email is loubenslouis@live.com"
pattern2 = r'([\w.-]+)@([\w.-]+)'
result7 = re.search(pattern2, email)
print(result7)
