# Morris In-Order Traversal Algorithm
## Summary
This algorithm will make [In Order Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) in space complexity of $O(1)$, which is the restriction of some problem like [94.Recover Binary Tree](https://leetcode.com/problems/recover-binary-search-tree/).

## Intuition
In in-order traversal, the order of traversing looks like this:
```c
traverse(root.left)
// do something here
traverse(root.right)
```
And in a BST, in-order traversal would guarantee a sorted list. 

However, if we do this in a stack or recursion, the worst-case space complexity could be $O(n)$ since we have to somehow remember the information of "parent" node so we can go back. Morris algorithm solved this problem by having the right-most pointer of the subtree pointing to the parent when it first encounters it and removing it the second time. And when that node is visited the second time, it means that we've already visited all of the left sub-tree and we can process the current node and go to right. 

So overall, it follows the left->current->right pattern of in-order traversal.

## Code
```python
def in_order(root):
  while root:
    # find the right-most node of left subtree
    temp = root.left
    if temp:
      while temp.right and temp.right != root:
        # keep going right 
        temp = temp.right
      if not temp.right:
        # the first time we encounter the right-most node
        # record parent's info on this node's right poitner
        temp.right = root
        # then we can process its left subtree
        root = root.left
      if temp.right == root:
        # the second time we encounter the right-most node
        # at this time, we've processed all the left subtree and can process the current node
        do_something(root)
        # also remember to remove the edge to convert the tree back
        temp.right = None
        # go to the right part
        root = root.right
    else:
      # no left node, means we can process the node
      do_something(root)


```