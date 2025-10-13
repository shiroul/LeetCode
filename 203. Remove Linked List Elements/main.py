# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if  not head:
            return head
        
        while head:
            if head.val != val:
                break
            head = head.next 

        if not head:
            return head
        
        prev = head
        current = head.next

        while current:
            if current.val != val:
                prev.next = current
                prev = current
            current = current.next
        prev.next = None
        return head
