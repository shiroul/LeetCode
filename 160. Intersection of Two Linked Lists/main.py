# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return 
        
        listA, listB = headA, headB

        while listA != listB:
            
            listA = listA.next if listA else headB
            listB = listB.next if listB else headA
    
        return listA