## Intuition
The idea is to count how many times **consecutive characters** in the string are the same as the previous one.

- Start by storing the **first character**.
- Iterate from index 1 to the end of the string.
- If the current character is the same as the previous one, increment the counter.
- If it's different, update the "previous" character.

---

## 💡 Approach

1. **Initialize** a variable `prev` with the first character of the input string.
2. **Initialize** the counter `count` with `1` to account for the first character.
3. **Iterate** through the string starting from index 1.
4. For each character:
   - If it is equal to `prev`, increment `count`.
   - If it is not equal, update `prev` with the current character.
5. **Return** the final count.

---

## Complexity

- **Time Complexity:**  
  \[
  O(n)
  \]  
  where \( n \) is the length of the input string. We traverse the string once.

- **Space Complexity:**  
  \[
  O(1)
  \]  
  We use only a few extra variables.

---

## Python Code

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        if not word:
            return 0  # Handle empty string case
        
        prev = word[0]
        count = 1  # Start with 1 to count the first character

        for ch in word[1:]:
            if ch == prev:
                count += 1
            else:
                prev = ch
        
        return count
