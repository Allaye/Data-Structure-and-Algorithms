#!/usr/bin/env python
# coding: utf-8

# In[107]:


class Queue:
    '''
    basic implememtation of a Queue, implement the basic properties of Queue.
    '''
    def __init__(self, item=[]):
        '''
        the class can be instanciated with a list or with no arguments
        '''
        self.items = item
        
    def enqueue(self, item):
        '''
        add new items to the add of an empty queue or non empty one, this occure at the button or the rear of the queue
        using the Last in Last in the queue
        '''
        self.items.insert(0, item)
    
    def isEmpty(self):
        '''
        return a bool true if nothing is in the queue
        '''
        return self.items == []
    
    def peek(self):
        '''
        return the top element of the queue, without modifying the queue
        '''
        if self.size() != 0:
            return self.items[(len(self.items)-1)]
        return None
    
    def size(self):
        '''
        return the size of the queue
        '''
        return len(self.items)
    
    def dequeue(self):
        '''
        remove items form the queue, this items is always the item return by the peek method,
        using the FIFO method
        '''
        if self.size() != 0:
            return self.items.pop()
        return None
    
    def clear(self):
        '''
        clear the queue of all items
        '''
        return self.items.clear()
        
    def __str__(self):
        '''
        return a string representation of the queue class
        '''
        return f'Data Structure of Queue has a size of {self.size()}'

