# 173. Binary Search Tree Iterator | [Link](https://leetcode.com/problems/binary-search-tree-iterator/)
## Idea
This problem uses a similar logic to question 230, [Kth Smallest Element in BST](https://github.com/lorenzoc25/LeetCodeNotes/blob/main/Trees/230KthSmallInBST.md). The overall ideaology is to use a stack to record the current smallest element, and whenever we call `next()`, we pop the element, return it and the next element will be the next smallest element. In other words, wee need to turn the BST into an ordered stack dynamically.

# Code
```py
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = deque()
        # initialize the stack
        while root:
            self.stk.append(root)
            root = root.left
        # by now, the top of the stack is the smallest element

    def next(self) -> int:
        # the next smallest will be on the top of the stack
        curr = self.stk.pop()
        returnVal = curr.val
        # if the node has a right ptr, we need to find the smallest value that is larger than this node
        curr = curr.right
        while curr:
            self.stk.append(curr)
            curr = curr.left
        return returnVal

    def hasNext(self) -> bool:
        # if the stack is empty, there's no more value we can find
        return True if self.stk else False
```