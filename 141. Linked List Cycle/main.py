# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = []
        current = head

        while current:
            if current in temp:
                return True
            temp.append(current)
            current = current.next
        return False