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
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        length = 0
        cur = self.head
        while cur.next != None:
            length +=1
            cur = cur.next
        return length
    
    def display(self):
        emum, cur = [], self.head
        while cur.next !=None:
            cur = cur.next
            emum.append(cur.data)
        print(emum)
        return emum
    
    def get(self, index):
        if index >=self.length():
            raise IndexError(f'Index out of range, linked list is of length {self.length()}')
        return self.display()[index]
        
    def delete(self, index):
        pass

