# -*- coding: utf-8 -*-

class List:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return str(self.value)   


class DoublyLinkedList:
    first = None
    last = None 
    
    
    def  __str__(self):
        sp_str = 'DLL: '
        current_element = self.first
        while current_element:
            sp_str += str(current_element) + ' '
            current_element = current_element.next
        return sp_str.rstrip()
    
    def push(self, value):
        if self.last is None:
            lt = List(value)
            self.first = lt
            self.last = lt
        else:
            lt = List(value, prev=self.last)
            self.last.next = lt
            self.last = lt 
    
    def pop(self):
        if self.last is None:
            pass
        elif self.last == self.first:
            self.first = None
            self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None
    
    def shift(self):
        if self.first is None:
            pass
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
                    
    def unshift(self, value):
        if self.first is None:
            lt = List(value)
            self.first = lt
            self.last = lt
        else:
            lt = List(value, next=self.first)
            self.first.prev = lt
            self.first = lt


"""
spisok = DoublyLinkedList()
spisok.unshift(3)
spisok.pop()
spisok.push(1)
spisok.push(2)
spisok.unshift('str')
spisok.unshift(7)
spisok.shift()
print(spisok)
"""
