#!/usr/bin/env python
# coding: utf-8


def factorial(n):
    if(n == 0):
        return 1
    return n*factorial(n-1)



def cumulative_sum(n):
    if(n == 0):
        return 0
    return n + cumulative_sum(n-1)


def word_split(phrase, list_of_word, output=None ):
    if(output == None):
        output = []
        
    for word in list_of_word:
        if phrase.startswith(word):
            
    