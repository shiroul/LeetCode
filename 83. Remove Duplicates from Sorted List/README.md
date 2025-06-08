# Intuition

We use two pointers: one (`current`) to track the current node, and another (`previousNode`) to track the node just before the current one.  
The idea is to compare the value of `current` with `previousNode`.  
If they are equal, it means there's a duplicate — so we update `previousNode.next` to skip the `current` node, effectively deleting it from the linked list.

---

# Approach

1. **Define Pointers:**
   - `current`: Tracks the node currently being processed.
   - `previousNode`: Tracks the node just before the `current` node.

2. **Iterate through the list:**
   - Start from the second node (`head.next`).
   - For each iteration:
     - If `current.val == previousNode.val`, it's a duplicate — skip `current` by linking `previousNode.next` to `current.next`.
     - Otherwise, move `previousNode` to `current`.
   - Always move `current` to the next node.

---

# Complexity

- **Time complexity:** `O(n)` — where `n` is the length of the linked list. Each node is visited once.
- **Space complexity:** `O(1)` — constant space, no extra data structures used.

---

# Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        previousNode = head
        current = head.next

        while current:
            if current.val == previousNode.val:
                previousNode.next = current.next  # Skip the duplicate
            else:
                previousNode = current  # Move to next unique node
            current = current.next

        return head
