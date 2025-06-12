### 💡 Intuition
The idea is to reverse the connections in a singly linked list. Normally, a list is structured as:  
`head -> node1 -> node2 -> ... -> tail -> None`  
We aim to reverse the connections so that it becomes:  
`None <- tail <- node2 <- node1 <- head`  
This means each node should point to its previous node instead of the next one.

---

### 🧭 Approach
We use an iterative approach to reverse the list in-place:

1. Initialize two pointers: `prev` as `None` (since the new tail should point to `None`) and `current` as `head`.
2. Traverse the list:
   - Temporarily store the next node using `temp = current.next`.
   - Reverse the current node’s pointer: `current.next = prev`.
   - Move the `prev` and `current` pointers one step forward.
3. When the loop ends, `prev` will point to the new head of the reversed list.
4. Return `prev` as the new head.

---

### ⏱️ Complexity

- **Time complexity:** $$O(n)$$ — We visit each node exactly once.
- **Space complexity:** $$O(1)$$ — We use only a constant amount of extra space.

---

### 🧩 Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temp = current.next      # Store next node
            current.next = prev      # Reverse the link
            prev = current           # Move prev forward
            current = temp           # Move current forward

        return prev                  # New head of the reversed list
