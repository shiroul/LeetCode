# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            current = head.next
        else:
            return head

        previousNode = head

        while current:
            if current.val == previousNode.val:
                current = current.next
                previousNode.next = current
            else:
                previousNode = current
                current = current.next
        return head