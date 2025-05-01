class MinStack:

    def __init__(self):
        self.data = []

        
    def push(self, x):
        if not self.data or x < self.data[-1][1]:self.data.append([x,x])
        else:self.data.append([x, self.data[-1][1]])
        
    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1][0]

    def getMin(self):
        return self.data[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()