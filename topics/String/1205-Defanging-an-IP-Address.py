############################################################
# Problem  : Defanging an IP Address
# ID       : 1205
# Difficulty: Easy
# Tags     : String
# Runtime  : 43
# Memory   : 19040000
# Language : Python3
# Solved   : 2026-06-22 08:10
# URL      : https://leetcode.com/problems/defanging-an-ip-address/
############################################################
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
        