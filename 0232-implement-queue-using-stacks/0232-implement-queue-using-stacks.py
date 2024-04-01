class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = 0

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
            
    def pop(self) -> int:
        res = self.s1.pop()
        if self.s1:
            self.front = self.s1[-1]
        return res
        

    def peek(self) -> int:
        return self.front;

    def empty(self) -> bool:
        return len(self.s1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()