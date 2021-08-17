
// approach: use stack to record the each character and its frequency
// if there's a character that has k frequency, we disgard it
class Solution {
public:
    string removeDuplicates(string s, int k) {
    stack<pair<char,int>> st;
    for (char c: s) // traverse through the string
    {
        if(!st.empty() && st.top().first == c) // same character, increase frequenct
        {
            st.top().second ++;
            if(st.top().second == k) // remove if it has the k frequenct
                st.pop();
        }
        else{
            st.push({c,1});
        }
    }
    // by the end of the process, the stack would contain the desired string but in reversed order
    // we also need to decode the string
    string res ="";
    while(!st.empty())
    {
        while(st.top().second != 0)
        {
            res += st.top().first;
            st.top().second --;
        }
        st.pop();
    }
    reverse(res.begin(),res.end());
    return res;
}
};
