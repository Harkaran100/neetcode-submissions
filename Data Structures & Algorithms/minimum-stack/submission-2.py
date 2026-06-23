class MinStack:
    # support 4 operations
    
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,val: int):
        self.stack.append(val)

        # check if empty
        if not self.minStack:
            self.minStack.append(val)
        elif val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
            
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
    