# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Traverse to the middle node
        middle_index = length // 2  # If even, it gives the second middle
        current = head
        for _ in range(middle_index):
            current = current.next
        
        return current