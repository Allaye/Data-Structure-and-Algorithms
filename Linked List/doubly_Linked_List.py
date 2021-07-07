#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# In[56]:


class DoublyLinkedList:
    
    def __init__(self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        if(self.head.data is None):
            self.head = new_node
            return
        cur = self.head
        while(cur.next != None):
            cur = cur.next
        new_node.prev = cur
        new_node.next = None
        cur.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        if(self.head.data is None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
            
    def erase(self, index):
        pass
    
    def length(self):
        if(self.head.data is None):
            print(f'Liked List is Empty')
            return
        enum, cur = [], self.head
        while(cur.next is not None):
            enum.append(cur.data)
            cur = cur.next
        enum.append(cur.data)
        return len(enum)
    
    def display(self, display='P'):
        if(self.head.data is None):
            print(f'Linked List is empty')
            return None
        enum, cur = [], self.head
        while(cur.next is not None):
            enum.append(cur.data)
            cur = cur.next
        enum.append(cur.data)
        if(display=='P'): print(enum)
        else: return enum
    
    def get(self, index):
        '''
        get the element inside the linked list with the index provided, raise error if not appr
        '''
        if(index >= self.length()):
            raise IndexError(f'Index provided is out of range of {self.length()}')
            return
        return self.display('R')[index]
        
    


# In[ ]:




