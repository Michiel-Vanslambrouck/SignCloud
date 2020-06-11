# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:38:50 2019
Python 3.6
@author: mcmic
"""

import re

data=open(r'signOutput.txt','r')
out=open(r'out.txt','w')
text=list(data)

List = []
for line in text:
    found = re.findall("\([-]?[\d]+ [-]?[\d]+ [-]?[\d]+\)",str(line))
    if len(found) > 0:
        List.append(found[0])

List2 = [str(coord).strip("\(\)") for coord in List if len(str(coord)) > 5]
[out.write(part+"\n") for part in List2]

data.close()
out.close()








