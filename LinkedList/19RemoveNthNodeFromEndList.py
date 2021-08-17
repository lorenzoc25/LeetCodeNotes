class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # idea: to use 2 pointer technique
        # let the first pointer run n position in advance then start the second pointer
        # let those 2 pointers advance simultaneously, if the first pointer reaches the end, then
        # the second pointer would arrive at the desired position
        first = head
        prev = None
        index = 0
        while index < n:
            first = first.next
            index += 1
        second = head
        while first and second:
            first = first.next
            prev = second
            second = second.next
        # at this time, second points to the node we want to delete
        if not prev:
            # the only time that prev is none is that there's only 1 element
            head = head.next
            return head
        prev.next = second.next
        return head
