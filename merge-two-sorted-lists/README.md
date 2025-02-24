# Intuition
The idea is to make new ListNode called dummy then copy it to another variable called current, so we can change the value of the list but able to keep track the head inside dummy. then we loop through the list1 and list2 untill we reach any of the list had value of None. after that we check the value of the list using .val and coppy the list who had the smallest value to the end of dummy list. repeat till we reach None value then break the loop. after that attach the remaning list in the end of the dummy list
# Approach
1. Define variable
    - we define empty ListNode and call it dummy
    - copy dummy to other variable called current so we can change the value without loosing the head
2. Loop Through the list
Loop till we get None Value from current value of list1 or list2

3. Check Value
`list1.val < list2.val` this code will check the current value of list1 and current value of list 2 then keep the smallest then attach it to the end of dummy list using `current.next = (list with smallest value)`. repeat it until we get None Value

4. Attach the remaning list to the end of the list using `current.next = list1 if list1 else list2`
5. return dummy value without head using `return dummy.next`

# Complexity
- Time complexity: O(n)
n = sum of both list lenght

- Space complexity: O(n)
n = sum of both list lenght

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next

```