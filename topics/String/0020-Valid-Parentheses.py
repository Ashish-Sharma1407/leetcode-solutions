############################################################
# Problem  : Valid Parentheses
# ID       : 20
# Difficulty: Easy
# Tags     : String, Stack
# Runtime  : 1
# Memory   : 19340000
# Language : Python3
# Solved   : 2026-07-23 11:41
# URL      : https://leetcode.com/problems/valid-parentheses/
############################################################
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False

        return len(stack) == 0