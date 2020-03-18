class Stack:

    def __init__(self):
        self.items = []


    def push(self, item):
        if len(self.items)==0:
            self.items.append(item)
        elif item<=self.items[0]:
            self.items.insert(0,item)
        else:
            self.items.append(item)


    def pop(self):
        item = None
        if len(self.items)==0:
            pass
        else:
            item = self.items.pop(0)
        return item


    def min(self):
        if len(self.items)==0:
            return None
        return self.items[0]

stack = Stack()
stack.push(3)
stack.push(1)
stack.push(5)
print(stack.items)