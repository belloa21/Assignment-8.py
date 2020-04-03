# Alex Bello
# 3/26/2020
# The stack and queue classes are stored here


class Qty_Stack:
    def __init__(self):
        self.qty = []

    def push(self, data):
        self.qty.append(data)

    def pop(self):
        return self.qty[-1]


class Price_Stack:
    def __init__(self):
        self.price = []

    def push(self, data):
        self.price.append(data)

    def pop(self):
        return self.price


class Qty_Queue:
    def __init__(self):
        self.qty = LinkedListTail()

    def push(self, data):
        self.qty.push_end(data)

    def pop(self):
        return self.qty.pop_end()

class Price_Queue:
    def __init__(self):
        self.price = LinkedListTail()

    def push(self, data):
        self.price.push_end(data)

    def pop(self):
        return self.price.pop_end()


class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def push_head(self, data):
        new_node = ListNode(data=data)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail = self.head

    def push_end(self, data):
        new_node = ListNode(data=data)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = self.head

    def pop_head(self):
        new_node = self.head
        self.head = new_node.next
        return new_node.data

    def pop_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data
