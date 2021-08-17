[Link](https://leetcode.com/problems/populating-next-right-pointers-in-each-node)<br/>

I used 2 approaches to solve the problem, one is using recursion and one is iterative using level-order traversal.
# Recursion
  idea: to define a helper function that allows us to pass in 2 nodes and connect them, and then let recursion do its work
```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        def connect2Nodes(node1,node2):
            if not node1 or not node2: return
            node1.next = node2
            node2.next = None
            connect2Nodes(node1.left,node1.right)
            connect2Nodes(node1.right,node2.left)
            connect2Nodes(node2.left,node2.right)
            
        connect2Nodes(root.left,root.right)
        return root
```

# iteratively
  idea: to use technique from [Problem#102](https://github.com/lorenzoc25/LeetCodeNotes/blob/main/102LevelOrderTraversal.md) and modify each level accordingly
```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        def levelOrder(root):
            q = deque()
            res = []
            q.append(root)
            while q:
                currLevel = []
                for i in range(len(q)):
                    node = q.popleft()
                    if node:
                        currLevel.append(node)
                        q.append(node.left)
                        q.append(node.right)
                currLevel and res.append(currLevel)
            return res
        
        nodes = levelOrder(root) # get the levels
        for lvl in nodes:
            lvl[-1].next = None # change the last one, then connect them
            for i in range(len(lvl)-1):
                lvl[i].next = lvl[i+1]
        return root
                        
```
