# [Link](https://leetcode.com/problems/reverse-nodes-in-k-group/)
# Idea
The question asked us to reverse nodes in group of K. So if we want to break them down, we just need to reverse the first k nodes, then the second group of k nodes 
and so on. Thus, we can just use recursion to help us do the work. <br/>
on each recursion call, we need to do the following
- reverse k nodes
- call the function again to recursively deal with the rest
and for base cases, we have:
- if the head given is null, we return null
- if the list given has a node less than k, return the head without modify.
To do the reverse k nodes, we can just use the same mehtod that we used to reverse the whole linked list like
```python
    def reverse(start):
        prev,curr= None,start
        while curr: # while curr != end
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```
to reverse only k list, we can add another argument and make sure to pass in the ending node, so we can change the while loop to 
```python
while curr != end:
```
and after doing that, we can implement the solution
```python
class Solution:
    def reverseN(self,start,end):
        prev,curr= None,start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None # base case 1
        temp = head
        for i in range(k):
            if not temp: return head # base case 2
            temp = temp.next
        newHead = self.reverseN(head,temp)
        # currently, head still points to the old head, so it will be the tail of the current reversed group
        head.next = self.reverseKGroup(temp,k) # reverse the rest of temp using temp, since temp points to the k + 1 node
        return newHead

```
