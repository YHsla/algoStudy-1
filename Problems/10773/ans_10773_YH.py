# https://www.acmicpc.net/problem/10773

# def solve():######
    
#Stack 구현
# class Stack(list):
#     def __init__(self):
#         self.stack=[]
        
#     def push(self, data):
#         self.stack.append(data)
        
#     def pop(self):
#         if self.is_empty():
#             return -1
#         else:
#             self.stack.pop()
            
#     def peak(self):
#         return self.stack[-1]
    
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         return False    

#Singly Linked list를 활용한 Stack 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data
    def is_empty(self):
        if len(self.head):
            return True
        return False
    def peak(self):
        if self.is_empty():
            return -1
        return self.head.data
    
            
        