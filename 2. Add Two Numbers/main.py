# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        prev = head
        carry = 0

        
        while l1 or l2 or carry:
            temp = 0

            if l1:
                temp+= l1.val
                l1 = l1.next
            if l2:
                temp+=l2.val
                l2 = l2.next
            
            if carry:
                temp += carry
            
            carry = temp // 10
            temp = temp % 10

            current = ListNode(temp)
            prev.next = current
            prev = current
        
        return head.next
            
            
            
            