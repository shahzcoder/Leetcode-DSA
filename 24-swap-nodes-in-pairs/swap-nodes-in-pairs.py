# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        while curr is not None and curr.next is not None:
            curr.val , curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        
        return head