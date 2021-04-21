

import ctypes


class DynamicArray():
    ### The idea is to create an array that grows based on the new element added to it. 
    
    def __init__(self):
        # instaciate the 
        self.length = 0
        self.capacity = 1
        self.array = self.raw_array(self.capacity)
        
    def __len__(self):
        # returning the length of the dynamic array, at first will be zero but will change as the list gets populated
        return self.length
    
    def __getitem(self, index):
        
        if not 0 <= index < self.length:
            return IndexError('Index is out of bound')
        return self.array[index]
    
    def append(self, element):
        
        if self.length == self.capacity:
            self._resize(2*self.capacity)
        self.array[self.length] = element
        self.length +=1
        
    def _resize(self, size):
        
        brray = self.raw_array(size)
        for i in range(self.length):
            brray[i] = self.array[i]
        self.array = brray
        self.capacity = size
        
    def raw_array(self, size):
        
        return (size * ctypes.py_object)()
            
    
    