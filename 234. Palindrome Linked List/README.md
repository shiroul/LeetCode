# 🧠 Intuition  
A linked list supports only one-way traversal, making it difficult to directly check for palindromes (which require comparing elements from both ends). To overcome this, we can copy all the values from the linked list into a Python list, which supports indexing and reverse traversal. Then we simply check if that list is a palindrome.

---

# 🚀 Approach  
1. Initialize an empty list to store node values.  
2. Traverse the linked list and append each node’s value to the list.  
3. After the traversal, use a two-pointer technique or reverse comparison to check if the list is a palindrome.  
4. Return `True` if all corresponding elements match; otherwise, return `False`.

---

# ⏱️ Complexity  
- **Time complexity:** $$O(n)$$  
  We traverse the entire linked list once to copy the values and then iterate half the list to check for palindrome.

- **Space complexity:** $$O(n)$$  
  We store all the node values in an additional list.

---

# 💻 Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False  # or True depending on how you treat an empty list

        values = []

        # Step 1: Copy linked list values into a list
        while head:
            values.append(head.val)
            head = head.next

        # Step 2: Check if the list is a palindrome
        for i in range(len(values) // 2):
            if values[i] != values[-(i + 1)]:
                return False

        return True
