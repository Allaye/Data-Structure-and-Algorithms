#!/usr/bin/env python
# coding: utf-8

# In[105]:


class Deque:
    '''
    implementation of a deques with its basic attribute
    
    '''
    def __init__(self, item=[]):
        '''
        the class can be instanciated with a list or with no arguments
        '''
        self.items = item
        
    def addFront(self, item):
        '''
        add item to the front of the deck, and return the item added
        '''
        if self.size() != 0:
            return self.items.insert(0, item)
        return self.items.append(item)
    
    def addRear(self, item):
        '''
        add items to the back of the deck, and return the item added
        '''
        return self.items.append(item)
    
    def removeFront(self):
        '''
        remove items form the front of the deck
        '''
        return self.items.pop(0)
    
    def removeRear(self):
        '''
        remove items from the back of the deck
        '''
        return self.items.pop()
    
    def peekFront(self):
        '''
        return the first element in the deck, without modifying the deck
        '''
        if self.size() != 0:
            return self.items[0]
        return None
    
    def peekRear(self):
        '''
        return the rear element in the deck, with modifying the deck
        '''
        if self.size() != 0:
            return self.items[-1]
        return None
        
    
    def isEmpty(self):
        '''
        this method checks if the deck is empty or not and return a bool value
        '''
        return self.items == []
    
    def size(self):
        '''
        return the len of the deck
        '''
        return len(self.items)
        
    

