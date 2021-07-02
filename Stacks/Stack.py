#!/usr/bin/env python
# coding: utf-8

# In[117]:


class Stack():
    '''
    implementation of a dynamic stack data structure, with its primary operations
    '''
    
    def __init__(self, values=[]):
        '''
        pass the default values the stack shout contain to the constructor, if more than
        one value use a list.
        '''
        self.items = values
    
    def isEmpty(self):
        '''
        check if the stack is empty, return a boolen value
        '''
        return self.items == []
    
    def push(self, item):
        '''
        add new items to the top of the stack
        '''
        return self.items.append(item)
    
    def pop(self):
        '''
        remove items from the stack this is done in a last in first out (LIFO) method, and return the item removed
        '''
        if self.size() != 0:
            return self.items.pop()
        return None
    
    def peek(self):
        '''
        return the last element added to the stack
        NB: this method does not modify the stack in anyway.
        '''
        if self.size() != 0:
            return self.items[-1]
        return None
    
    def size(self):
        '''
        get the len of the stack
        '''
        return len(self.items)
    
    def clear(self):
        '''
        remove all the items in the stack returning an empty stack, which perform new operation on
        '''
        return self.items.clear()
    
    def __str__(self):
        return self.size()