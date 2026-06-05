from queue import Queue
class MyQueue:

    def __init__(self):
        self.q = Queue(maxsize = 0)
        

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        return self.q.get()
        

    def peek(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()