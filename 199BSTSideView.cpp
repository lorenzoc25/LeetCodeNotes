// used the level order traversal algorithm provided last time
// basically the side view just contains the last element of each order
// so we just need to level order traverse through it and we are done

class Solution
{
public:
    vector<int> rightSideView(TreeNode *root)
    {
        vector<vector<int> > lvl = levelOrder(root); // level order traverse thri
        vector<int> res;
        for (auto v : lvl) // get each level's last element
            res.push_back(v[v.size() - 1]);
        return res;
    }

    vector<vector<int> > levelOrder(TreeNode *root)
    {
        vector<vector<int> > ans;
        helper(root, 0, ans);
        return ans;
    }

    void helper(TreeNode *curr, int level, vector<vector<int> > &ans)
    {
        if (!curr)
            return;
        if (ans.size() == level) // need allocate new space
            ans.push_back(vector<int>{});
        ans[level].push_back(curr->val);
        helper(curr->left, level + 1, ans);
        helper(curr->right, level + 1, ans);
    }
};