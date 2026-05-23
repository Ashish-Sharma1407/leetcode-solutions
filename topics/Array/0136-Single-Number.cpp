////////////////////////////////////////////////////////////
// Problem  : Single Number
// ID       : 136
// Difficulty: Easy
// Tags     : Array, Bit Manipulation
// Runtime  : 0
// Memory   : 20696000
// Language : C++
// Solved   : 2025-08-11 22:25
// URL      : https://leetcode.com/problems/single-number/
////////////////////////////////////////////////////////////
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(int num: nums){
            ans ^= num;
        }
        return ans;
    }
};