class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return f"{self.data}"

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


class queue_two_stacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enQueue(self, value):
        self.stack1.push(value)

    def shift_queue(self):
        if(self.stack2.size() == 0):
            while(self.stack1.size() != 0):
                self.stack2.push(self.stack1.pop())

    def deQueue(self):
        self.shift_queue()
        return self.stack2.pop()


stack_queue = queue_two_stacks()

stack_queue.enQueue(3)
stack_queue.enQueue(1)
stack_queue.enQueue(10)
stack_queue.enQueue(5)

# stack_queue.stack1.print()
# print("%"*20)
print(stack_queue.deQueue())
# print("%"*20)
# stack_queue.stack1.print()
# stack_queue.stack2.print()

stack_queue.enQueue(2)

print("stack 1")
stack_queue.stack1.print()
print("stack 2")
stack_queue.stack2.print()
print(stack_queue.deQueue())