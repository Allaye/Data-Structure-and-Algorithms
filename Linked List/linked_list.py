#!/usr/bin/env python
# coding: utf-8

# In[39]:


class Node:
    '''
    implementation of the core struture of the Linked list node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None


# In[125]:


class LinkedList:
    '''
    Implementation of operation that can be performed with a linked list
    
    '''
    def __init__(self, data=None):
        self.head = Node()
        
    def append(self, data):
        '''
        add new item to the linked list
        '''
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        '''
        return the length of the linked list
        '''
        length = 0
        cur = self.head
        while cur.next != None:
            length +=1
            cur = cur.next
        return length
    
    def display(self, display='P'):
        '''
        display or return all the element in the linked list based on the argument provided, default is to print
        '''
        emum, cur = [], self.head
        while cur.next !=None:
            cur = cur.next
            emum.append(cur.data)
        if(display=='P'): print(emum)
        else: return emum
    
    def get(self, index):
        '''
        return a linked list value based on the index provided
        '''
        if index >=self.length():
            raise IndexError(f'Index out of range, linked list is of length {self.length()}')
        return self.display()[index]
        
    def erase(self, index):
        '''
        delete element from the linked list based on the index provided.
        '''
        if(index >= self.length()):
            raise IndexError(f'Index out of range, linked list is of length {self.length()}')
        cur_index = 0
        cur = self.head
        while(True):
            temp = cur
            cur = cur.next
            if(cur_index == index):
                temp.next = cur.next
                return
            cur_index +=1

