# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # use slow and fast pointer to reach the middle
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # compare the first half and reverse the second half
        left , right = head , prev
        
        # compare till the end of second half
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next

        return True