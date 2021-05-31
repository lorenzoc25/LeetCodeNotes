# 617 Merge binary trees

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
       # case 1, the current nodes are both None
        if not root1 and not root2:
            return None
       # case 2, one node is None
        elif not root1:
            return root2
        elif not root2:
            return root1

        # from here, we can assume that both nodes are valid and just perform addition
        root1.val += root2.val
        # then we process the childrens
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        # and return
        return root1

# 104 Maximum Depth of a tree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # we've reached the leaf node
        if not root:
            return 0
        # 1 is account for the current depth, and we want to find the maximum from both children's depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# also, we can one-liner this problem
# return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right)) if root else 0


# 226 Invert Binary Trees
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root:
            return
        # idea: only care about swapping the current node's children, then let recursion to care about the rest
        # so this is a pre-order traversal
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# 101 Symmetric Tree
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.comp(root.left, root.right)

    # we need to define a helper function to help us compare 2 nodes
    def comp(self, root1, root2):
        # both root reaches an end
        if not root1 and not root2:
            return True
        # only 1 node reaches the end
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        # compare the left child of the left child passed in and the right child of the right child pass in (outer)
        # also compare for inter
        return self.comp(root1.left, root2.right) and self.comp(root1.right, root2.left)
