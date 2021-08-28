# Copy List with Random Pointer | [Link](https://leetcode.com/problems/copy-list-with-random-pointer/)
## Idea
We can simply do this probelm by traversing the list two times.  
The first time we can just make a copy of the list without caring about the random pointer while record some infomation, and in the second traversal, we can add those random pointers in using the infomation we gathered from the first traversal.  

So what kind of information do we need to gather? Since we are dealing with linked list, we can't directly access the index of each node, so first we need to know the index of each node. So during the traversal, we can use a hash map to record the index and the node we construct. 

However, that is not enough. During the second loop, when we need to add those random pointers in to the newly formed list, all the information we have is the random pointer from the old list and the indexes of the new list nodes. We need to find a way to know the index of the old list too. So that's why we need a second hash map to record the old list node to the old index. And with those infomation, we can easily solve the problem.

## Code
```py
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        newList = Node(0)
        idxToNode = {} # for the newly formed list
        nodeToIdx = {} # for the old list
        temp = head
        idx = 0
        new_trav = newList
        # copy the linked list first and record the position of each node
        while temp:
            new_trav.val = temp.val
            nodeToIdx[temp] = idx
            idxToNode[idx] = new_trav
            temp = temp.next
            # if this is not the last node
            if temp:
                new_trav.next = Node(0)
                new_trav = new_trav.next
                idx += 1
        
        temp,new_trav = head,newList
        # now we add all the random pointer into the list
        while temp:
            if not temp.random:
                new_trav.random = None
            else:
                new_trav.random = idxToNode[nodeToIdx[temp.random]]
            temp = temp.next
            new_trav = new_trav.next
        
        return newList
```