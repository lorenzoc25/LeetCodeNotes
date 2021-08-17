[Link](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
## Explaination
Idea: to let recursion do its work
We can break down the problem into 3 phases:
- We flatten the left and right subtree first
- We set the flattened left subtree to the right and change the left to null
- We add the old right subtree to the back of the old left subtree (the new right subtree)

To visualize the proecss:
```
Original Tree:
         1
        / \
       2    5
      / \    \
     3   4    6  

Step1:
         1
        / \
       2    5
        \    \
         3    6  
          \
           4
Step2:
         1
          \      placeHolder
            2       \
             \       5
              3       \
               \       6
                4     
Step3:
         1
          \      
            2     
             \      
              3      
               \     
                4
                 \
                  5
                   \
                    6    
```
We can let recursion handle the first step easily since we've broken the problem down into a smaller one, then we can simply perform the step2 and 3 by ourselves. 

## Code
```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)

        currLeft,currRight = root.left, root.right
        root.right = currLeft
        root.left = None
        # traverse down the right path after we shift the left over
        temp = root
        while temp.right:
            temp = temp.right 
        # after the loop, temp points to the end of the left subtree
        temp.right = currRight
```