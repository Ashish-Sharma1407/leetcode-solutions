////////////////////////////////////////////////////////////
// Problem  : Next Greater Element I
// ID       : 496
// Difficulty: Easy
// Tags     : Array, Hash Table, Stack, Monotonic Stack
// Runtime  : 1
// Memory   : 12712000
// Language : C++
// Solved   : 2025-06-28 22:08
// URL      : https://leetcode.com/problems/next-greater-element-i/
////////////////////////////////////////////////////////////
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        unordered_map<int, int> m;
        vector<int> ans(nums1.size(), 0);
        stack<int> s;
        
        int n = nums2.size() - 1;
        for(int i = n; i >= 0; i--){
            while(s.size() > 0 && s.top() <= nums2[i]){
                s.pop();
            }
            if(s.empty()){
                m.emplace(nums2[i], -1);
            } else{
                m.emplace(nums2[i], s.top());
            }
            s.push(nums2[i]);
        }
        for(int i = 0; i < nums1.size(); i++){
            if(m.find(nums1[i]) != m.end()){
                ans[i] = m[nums1[i]];
            }
        }
        return ans;
    }
};