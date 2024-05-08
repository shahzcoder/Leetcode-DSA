# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or 
            head.next is None): 
            return

        slow_Ptr = head 
        fast_Ptr = head 

        prev = None

        while (fast_Ptr is not None and 
               fast_Ptr.next is not None): 
            fast_Ptr = fast_Ptr.next.next
            prev = slow_Ptr 
            slow_Ptr = slow_Ptr.next

        prev.next = slow_Ptr.next
        return head        
        