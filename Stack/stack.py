class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if not self.top:
            self.top = node
        else:
            #print("top ",self.top.data)
            node.next = self.top
            self.top = node
            #print("top ",self.top.next)

        self.size +=1

    def pop(self):
        if not self.top:
            print("Stack is empty. Nothing to pop.")

        else:
            print("Data popped: ", self.top.data)
            self.top = self.top.next

    def print_stack(self):
        current = self.top
        print("Stack:")
        while(current):
            print(current.data)
            current = current.next
    
# stack1 = Stack()
# stack1.push(1)
# stack1.push(2)
# stack1.print_stack()
# stack1.pop()
# stack1.print_stack()
