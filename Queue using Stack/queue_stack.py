#Implement the functions of Queue using Stack Data Structure
import stack as st

class Queue:
    def __init__(self):
        self.queue1 = st.Stack()
        
    def enqueue(self, data):
        self.queue1.push(data)

    def dequeue(self):
        if not self.queue1.top:
            print("Queue is empty. Nothing to dequeue.")

        else:
            queue2 = st.Stack()
            x = self.queue1.top
            while(x):
                queue2.push(x.data)
                x = x.next
            print("Data removed: ", queue2.pop())

            x = queue2.top
            while(x):
                queue1.enqueue(x.data)
                x = x.next
    def remove_all(self):
        self.
    def print_queue(self):
        if not self.queue1.top:
            print("Queue is empty. Nothing to dequeue.")

        else:
            queue2 = st.Stack()
            x = self.queue1.top
            while(x):
                queue2.push(x.data)
                x = x.next
            current = queue2.top
            print("Queue:")
            while(current):
                print(current.data)
                current = current.next
    
queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.print_queue()
queue1.dequeue()
queue1.print_queue()
