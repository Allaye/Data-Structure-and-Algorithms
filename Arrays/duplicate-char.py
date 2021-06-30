#!/usr/bin/env python
# coding: utf-8

# In[29]:


def check_duplicate(string):
    """
    use set to detect duplicate values and if the len of 
    set is not equal len of string there is a duplicate
    """
    return (len(string) == len(set(string)))


# In[55]:


def check_duplicate2(string):
    '''
    create a copy of the word and convert it into an array
    loop through on of them and remove the value from the other array
    check if there is another element of the same time inside the array
    if there is you have a duplicate.
    '''
    control = words = list(string)
    for i, w in enumerate(words):
        control.pop(i)
        if w in control:
            return False
        return True


# In[63]:


def check_duplicate3(string):
    chars = set()
    for s in string:
        if s in chars:
            return False
        else:
            chars.add(s)
    return True

