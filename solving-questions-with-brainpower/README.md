# Intuition
the idea is to try all posible option using recursive but to solve TLE problem we using dictionary to memorize any solved problem so we didnt solve same problem twice.
# Approach
1. define variable
    -  stop variable store value of index to make recursive stop
    - memo dict to store value so we didnt need to recalculate problem that we already finish it before

2. define takeOrSkip function
    - base case `if i >= stop:` will return 0 to stop the recursive
    - using this code `if i in memo:` to prevent calculate same problem twice
    - take value will store current solve value + recursive of `takeOrSkip(i+questions[i][1]+1`
    - skip value will continue recursive to `takeOrSkip(i+1)`
    - store memorize value with maximum value from take or skip
# Complexity
- Time complexity: O(n)

- Space complexity: O(n)


# Code
```python3 []
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        stop = len(questions)
        memo = {}


        def takeOrSkip(i):
            if i >= stop:
                return 0
            if i in memo:
                return memo[i]
            
            take = questions[i][0] + takeOrSkip(i+questions[i][1]+1)
            skip = takeOrSkip(i+1)

            memo[i] = take if take > skip else skip

            return memo[i]
        
        return takeOrSkip(0)

```