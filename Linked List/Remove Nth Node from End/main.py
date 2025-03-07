# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head
        fast_pointer = dummy
        slow_pointer = dummy 

        for _ in range(n+1):
            fast_pointer = fast_pointer.next

        
        while fast_pointer: 
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        

        slow_pointer.next = slow_pointer.next.next

        return dummy.next


        
        