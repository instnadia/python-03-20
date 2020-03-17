class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def deQueue(self):
        node = None
        if self.head == None:
            pass
        else:
            node = self.head
            self.head = self.head.next
        return node

    def enQueue(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = Node(value)

    def front(self):
        if self.head == None:
            return None
        else:
            return self.head

    def isEmpty(self):
        return self.head == None

    def contains(self, value):
        flag = False
        if self.head == None:
            pass
        else:
            runner = self.head
            while runner:
                if runner.data == value:
                    return True
                runner = runner.next
        return flag

    def size(self):
        count = 0
        if self.head == None:
            pass
        else:
            runner = self.head
            while runner:
                count += 1
                runner = runner.next
        return count