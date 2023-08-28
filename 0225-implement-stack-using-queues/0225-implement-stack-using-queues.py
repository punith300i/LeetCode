class MyStack:
    
    def __init__(self):
        self.top_val = None
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.top_val = x
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1)>1:
            self.top_val = self.q1.popleft()
            self.q2.append(self.top_val)
        popped_val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped_val

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return len(self.q1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()