############################################################
# Problem  : Backspace String Compare
# ID       : 874
# Difficulty: Easy
# Tags     : Two Pointers, String, Stack, Simulation
# Runtime  : 0
# Memory   : 19332000
# Language : Python3
# Solved   : 2026-07-04 21:12
# URL      : https://leetcode.com/problems/backspace-string-compare/
############################################################
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        self.stack1 = []
        self.stack2 = []

        for char in list(s):
            if char != "#":
                self.stack1.append(char)
            else:
                if len(self.stack1) == 0:
                    continue
                else:
                    self.stack1.pop()

        for char in list(t):
            if char != "#":
                self.stack2.append(char)
            else:
                if len(self.stack2) == 0:
                    continue
                else:
                    self.stack2.pop()
        
        return self.stack1 == self.stack2
         
        