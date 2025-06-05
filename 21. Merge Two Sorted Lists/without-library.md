# Intuition
The idea is to return the other list immediately if one of the input lists is `null`, since there's nothing to merge. Then, we choose the node with the smaller value between the two list heads as the starting point (`head`) of the merged list. From there, we iterate through both lists, always attaching the smaller node to the current position. Once one of the lists is fully traversed, we simply attach the remainder of the other list to the merged list. Finally, we return `head` as the result.

# Approach
1. **Base Cases**:  
   If one of the input lists is `None`, return the other list directly, since there's nothing to merge.

2. **Initialization**:  
   Determine the head of the new list by comparing the first values of `list1` and `list2`. Advance the pointer in the list from which the head node was taken.

3. **Merging**:  
   Iterate while both `list1` and `list2` are not `None`. Compare the current nodes, append the smaller one to the result list, and move the corresponding pointer forward.

4. **Remaining Nodes**:  
   Once one list is exhausted, append the remaining part of the other list, as it is already sorted.

5. **Return the merged list** starting from `head`.

# Complexity
- **Time complexity**:  
  $$O(n + m)$$  
  Where \( n \) and \( m \) are the lengths of `list1` and `list2`, respectively. Each node is visited exactly once.

- **Space complexity**:  
  $$O(1)$$  
  We are not using any additional space apart from a few pointers. The merging is done in-place.

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return head
