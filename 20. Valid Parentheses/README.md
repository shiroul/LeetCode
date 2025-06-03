# Intuition
the idea is to put the open bracket inside new list. make dictionary with closing bracket as the key and open bracket as the value, so everytime we get closing bracket we can check with dictionary for what opening bracket suit with that bracket

# Approach
1. Declare a new variable
    - make new dictionary and store closing bracket as key and opening bracket as value
    - make empty list to store opening bracket
2. Loop Through the string

    - first, `if x in inputDict:` we need to check if the character is exist inside dictionary. if not it will count as opening bracket, if yes it count inside this condition 
    - then, `if not temp:`check again if there any value inside the list. if there is none, it mean closing bracket appear before opening bracket then return False
    - if any value inside the list then we use this condition `if inputDict[x] == temp[-1]:` to check if the last index have opening bracket for current closing bracket. if not it will break the loop, if yes it will pop the list
    - if not all above this condition not meet, the current character will count as opening bracket then it will store inside the list.
3. Return Value
`return True if len(temp) == 0 else False` this code will check if there is any value inside  the list, it mean there is opening bracket without closing bracket then it will return False. but if there is none inside the list, it mean all opening bracket had the closing bracket with correct order

# Complexity
- Time complexity: O(n)
n = the lenght of the string, because it will loop through the list

- Space complexity: O(n)
 n = how many opening bracket inside the string, because it will store any opening bracket

# Code
```python3 []
class Solution:
    def isValid(self, s: str) -> bool:
        inputDict = {')': '(', ']': '[', '}': '{'}
        temp = []

        for x in s:
            if x in inputDict:
                if not temp:
                    return False
                if inputDict[x] == temp[-1]:
                    temp.pop()
                    continue
                break
            temp.append(x)
        
        return True if len(temp) == 0 else False
    
```