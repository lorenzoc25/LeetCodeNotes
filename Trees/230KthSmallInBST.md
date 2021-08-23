the first approach is kinda of cheating, the idea is to construct an array using in-order traversal and return the k-th element in the array since the BST must be in order
```py
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.arr = []

        # inorder traversal --- process left, then middle, then right
        # key point: inorder traversal in BST would guaranteed an ordered list
        def inOrd(root):
            if not root:
                return
            inOrd(root.left)  # left
            self.arr.append(root.val)  # middle, or current
            inOrd(root.right)  # right

        inOrd(root)
        return self.arr[k-1]
```
this approach's idea is to go to the smallest element (the farthest left) and then try to search from that on
```py
    def kSstack(self, root, k):
        # construct a root of left nodes since left is always the smaller one
        stk = []
        # keep trying this process of going to the most left
        while 1:
            while root:
                stk.append(root)
                root = root.left
            # after the loop, the stack's top contains the most left element now
            root = stk.pop()  # root is the smallest elemtne on the first loop
            k -= 1  # finding the next smaller element
            if k == 0:  # if we arrived the kth smallest element
                return root.val
            root = root.right  # go to the right node if possible due to the natural of BST
        return
```
