# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        temp = []

        while head:
            temp.append(head.val)
            head = head.next

        for x in range(len(temp)//2):
            if temp[x] != temp[-(x+1)]:
                return False
        return True