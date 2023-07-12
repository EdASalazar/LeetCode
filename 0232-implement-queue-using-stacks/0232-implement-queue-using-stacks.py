class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []
        

    def push(self, x: int) -> None:
        self.back.insert(0, x)
        

    def pop(self) -> int:
        if not self.front:
            while self.back:
                self.front.insert(0, self.back.pop(0))
        return self.front.pop(0)
        

    def peek(self) -> int:
        if not self.front:
            while self.back:
                self.front.insert(0, self.back.pop(0))
        return self.front[0]
        

    def empty(self) -> bool:
        return not self.front and not self.back


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()