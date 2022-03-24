# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:23:59 2022

@author: iernst
"""

#path = r"C:\Users\iernst\OneDrive - Intel Corporation\Documents\university\third year\semester B\intro Knowledge & Data"
#file="ex3_text.txt"

def read_line (n,file):
    if type(n) is not int:
        return ("invalid input detected")
    elif file !="ex3_text.txt":
        return ("file not found")
    fn=open(file)
    list1=[]
    count=0
    for line in fn:
        list1.append(line)
        count+=1
    if count<n:
        return (f"line {n} doesn't exist")
    else:
        return (list1[n-1])
        

#print(read_line(9, "ex3_text.txt")) 