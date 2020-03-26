# Alex Bello
# 3/26/2020
# The stack and queue classes are stored here


class Stack:
    def __init__(self):
        self.myList = []

    def push(self, data):
        self.myList.append(data)

    def pop(self):
        return self.myList[-1]


class Queue:
    def __init__(self):
        self.mylist = []

    def push(self, data):
        self.mylist.add_end(data)

    def pop(self):
        return self.mylist.remove_head()

