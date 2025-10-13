# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        current = head.next
        prev = head
        head.next = None

        while True:
            if not current:
                head = prev
                return head
            temp = current.next
            current.next = prev
            prev = current
            current = temp

            
        