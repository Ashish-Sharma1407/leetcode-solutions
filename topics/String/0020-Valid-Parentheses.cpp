////////////////////////////////////////////////////////////
// Problem  : Valid Parentheses
// ID       : 20
// Difficulty: Easy
// Tags     : String, Stack
// Runtime  : 0
// Memory   : 8772000
// Language : C++
// Solved   : 2025-06-26 22:17
// URL      : https://leetcode.com/problems/valid-parentheses/
////////////////////////////////////////////////////////////
class Solution {
public:
    bool isValid(string str) {
        stack <char> st;
        for(int i = 0; i < str.size(); i++){
            if(str[i] == '(' || str[i] == '{' || str[i] == '[' ){
                st.push(str[i]);
            } else{
                if(st.size() == 0){
                    return false;
                }
                if((st.top() == '(' && str[i] == ')') ||
                   (st.top() == '{' && str[i] == '}') ||
                   (st.top() == '[' && str[i] == ']')){
                    st.pop();
                } else{
                    return false;
                }
            }
        }
        return st.size() == 0;
    }
};