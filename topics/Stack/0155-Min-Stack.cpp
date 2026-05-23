////////////////////////////////////////////////////////////
// Problem  : Min Stack
// ID       : 155
// Difficulty: Medium
// Tags     : Stack, Design
// Runtime  : 3
// Memory   : 23192000
// Language : C++
// Solved   : 2025-06-30 16:11
// URL      : https://leetcode.com/problems/min-stack/
////////////////////////////////////////////////////////////
class MinStack {
public:
    stack<pair<int, int>> s;
    MinStack() {
        
    }
    
    void push(int val) {
        if(s.empty()){
            s.push({val, val});
        } else{
            int minVal = min(val, s.top().second);
            s.push({val, minVal});
        }
    }
    
    void pop() {
        s.pop();
    }
    
    int top() {
        return s.top().first;
    }
    
    int getMin() {
        return s.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */