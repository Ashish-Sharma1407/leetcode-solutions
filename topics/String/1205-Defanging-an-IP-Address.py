############################################################
# Problem  : Defanging an IP Address
# ID       : 1205
# Difficulty: Easy
# Tags     : String
# Runtime  : 43
# Memory   : 18940000
# Language : Python3
# Solved   : 2026-05-23 22:52
# URL      : https://leetcode.com/problems/defanging-an-ip-address/
############################################################
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in range(len(address)):
            if address[i] == ".":
                ans += "[.]"
            else:
                ans += address[i]
        return ans
        