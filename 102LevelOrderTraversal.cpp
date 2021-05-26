// this approach didn't use the typical queue apporach, instead, it uses recursion
// to make the whole code cleaner

class Solution
{
public:
    vector<vector<int> > levelOrder(TreeNode *root)
    {
        vector<vector<int> > ans;
        helper(root, 0, ans);
        return ans;
    }

    // the recursion function
    void helper(TreeNode *curr, int level, vector<vector<int> > &ans)
    {
        // typical base case
        if (!curr)
            return;

        // need allocate new space if the returning vector can't don't have enought spot
        if (ans.size() == level)
            ans.push_back(vector<int>{});
        // process he current val into the ans
        ans[level].push_back(curr->val);

        // by doing this, we can separate each level of nodes
        helper(curr->left, level + 1, ans);
        helper(curr->right, level + 1, ans);
    }
};