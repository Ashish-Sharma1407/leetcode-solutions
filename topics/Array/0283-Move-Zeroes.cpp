////////////////////////////////////////////////////////////
// Problem  : Move Zeroes
// ID       : 283
// Difficulty: Easy
// Tags     : Array, Two Pointers
// Runtime  : 0
// Memory   : 23860000
// Language : C++
// Solved   : 2025-06-27 01:32
// URL      : https://leetcode.com/problems/move-zeroes/
////////////////////////////////////////////////////////////
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int nonZeroIndex = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != 0){
                swap(nums[i], nums[nonZeroIndex]);
                nonZeroIndex++;
            }
        }
    }
};