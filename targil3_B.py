# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:35:52 2022

@author: iernst
"""

def longest_words (file):
    try:
        fn=open(file).read()
        for char in fn:
            if (char.isalpha()==False):
                fn= fn.replace(char,' ')
        divideText=fn.split()
        divideText.sort(key=len,reverse=True)
        return (divideText[0:5])
    except:
        print("file not found")
        return []

#print(longest_words("ex3_text.txt"))