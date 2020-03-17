class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self

    def pop(self):
        node = None
        if self.head == None:
            pass
        else:
            node = self.head
            self.head = self.head.next
        return node

    def peek(self):
        if self.head != None:
            return self.head
        else:
            return None

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

    def isEmpty(self):
        return self.head == None
    
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

    def print(self):
        if self.head == None:
            print("EMPTY")
        else:
            runner = self.head
            while runner:
                print(f"{runner.data} =>")
                runner = runner.next
            print("None")


stack = Stack()
stack.push(3)
stack.push(1)
stack.push(10)
# stack.print()
# print(stack.size())
# print(stack.isEmpty())
# print(stack.contains(10))
# print(stack.contains(11))