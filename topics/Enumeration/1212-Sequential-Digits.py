############################################################
# Problem  : Sequential Digits
# ID       : 1212
# Difficulty: Medium
# Tags     : Enumeration
# Runtime  : 0
# Memory   : 19232000
# Language : Python3
# Solved   : 2026-07-13 10:03
# URL      : https://leetcode.com/problems/sequential-digits/
############################################################
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        ans = []
        for length in range(2, 10): 
            for start in range(0, 10 - length):
                num = int(digits[start:start+length])
                if low <= num <= high:
                    ans.append(num)
        return ans