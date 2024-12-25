# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Find the position to stop before the node to remove
        position_to_stop = length - n

        # Step 3: Use a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        current = dummy

        # Step 4: Traverse to the node just before the one to remove
        for _ in range(position_to_stop):
            current = current.next

        # Step 5: Remove the nth node from the end
        current.next = current.next.next

        # Step 6: Return the modified list
        return dummy.next