class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)


    def pop(self) -> int:
        tempQueue = deque()
        while len(self.queue) > 1:
            tempQueue.append(self.queue.popleft())
        popVal = self.queue.popleft()
        self.queue = tempQueue
        return popVal
        

    def top(self) -> int:
        tempQueue = deque()
        while len(self.queue) > 1:
            tempQueue.append(self.queue.popleft())
        popVal = self.queue[0] # last value
        tempQueue.append(self.queue.popleft())
        self.queue = tempQueue
        return popVal
        

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()