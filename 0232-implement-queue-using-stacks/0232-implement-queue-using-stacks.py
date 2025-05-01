class MyQueue:

    def __init__(self):
        self.data = []
        

    def push(self, x):
        self.data.append(x) 

    def pop(self):
        front = self.data[0]
        self.data = self.data[1:]
        return front

    def peek(self):
        return self.data[0]

    def empty(self):
        return not bool(self.data)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()