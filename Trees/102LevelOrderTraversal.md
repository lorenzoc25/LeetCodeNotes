```c++
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
```
Now this is a regular iterative approach using queue

```python
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return
        q = deque()
        q.append(root)
        res = []
        while q:
            currLevel = []
            # idea: remember how many nodes are there in each level 
            for i in range(len(q)):
                # after we pop the node, we add the child of it
                node = q.popleft()
                if node:
                    currLevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            currLevel and res.append(currLevel)
        return res
```
