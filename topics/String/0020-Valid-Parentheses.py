############################################################
# Problem  : Valid Parentheses
# ID       : 20
# Difficulty: Easy
# Tags     : String, Stack
# Runtime  : 1
# Memory   : 19220000
# Language : Python3
# Solved   : 2026-07-04 20:05
# URL      : https://leetcode.com/problems/valid-parentheses/
############################################################
class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        if len(s) % 2 != 0:
            return False
        for char in list(s):
            if char == "(" or char == "{" or char == "[":
                self.stack.append(char)
            else:
                if len(self.stack) == 0:
                    return False
                item = self.stack.pop()
                if char == "}" and item != "{":
                    return False
                elif char == "]" and item != "[":
                    return False
                elif char == ")" and item != "(":
                    return False
        return len(self.stack)==0