""""
Implement a queue using two stacks. Your queue should have the following methods:"""

class myQueue:

    def __init__(self):
        # Initialize your data members
        self.main = []
        self.temp = []
        

    def enqueue(self, x):
        # Implement the enqueue operation
        while self.main:
            self.temp.append(self.main.pop())
            
        self.main.append(x)
        
        while self.temp:
            self.main.append(self.temp.pop())
        
    def dequeue(self):
        # Implement the dequeue operation
        if not self.main:
            return 
        return self.main.pop()


    def front(self):
        # Return the front element of the queue
        if not self.main:
            return -1
        return self.main[-1]


    def size(self):
        # Return the current size of the queue
        return len(self.main)
    

        
        
if __name__ == "__main__":
    queue = myQueue()
    queue.enqueue(1)
    queue.enqueue("A")
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.front())