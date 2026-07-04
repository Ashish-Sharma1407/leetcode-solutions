############################################################
# Problem  : Implement Queue using Stacks
# ID       : 232
# Difficulty: Easy
# Tags     : Stack, Design, Queue
# Runtime  : 0
# Memory   : 19440000
# Language : Python3
# Solved   : 2026-07-04 10:48
# URL      : https://leetcode.com/problems/implement-queue-using-stacks/
############################################################
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        
    def pop(self) -> int:
        x = self.stack1[-1]
        self.stack1.pop()
        return x

    def peek(self) -> int:
        return self.stack1[-1]
        
    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()