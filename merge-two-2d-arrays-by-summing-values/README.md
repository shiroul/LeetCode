# Intuition
The idea is to use two pointers to track the elements in both lists. We iterate through both lists simultaneously, comparing their elements. If the IDs match, we sum their values; otherwise, we add the smaller element to the output list. The loop terminates when either pointer reaches the end of its respective list.

# Approach
1. Initialize pointer and output list
- Define two pointer variables (first and second) to keep track the positions in nums1 and nums2.
- Create an empty list output to store the merged result.
2. Iterate both list
We iterate through both lists using a while loop, stopping when either pointer reaches the end of its list.
- Case 1: Matching ID
    - If `nums1[first][0] == nums2[second][0]`, both lists contain the same ID.
    - We sum their values and append [id, summed_value] to output.
    - We move both pointer forward by adding by 1
- Case 2: ID in nums1 is Smaller
    - If `nums1[first][0] < nums2[second][0]`, then append nums1[first] to output list.
    - Move the first pointer forward.
- Case 3: ID in nums2 is Smaller
    - If `nums1[first][0] > nums2[second][0]`, then append nums2[second] to output list.
    - Move the second pointer forward.

3. Append remaning Element
- If nums1 has remaining elements, append them to output.
- If nums2 has remaining elements, append them to output.
4. Return
give output list as return

# Complexity
- Time complexity: O(n)
n = len(nums1)+len(nums2)

- Space complexity: O(n)
n = len(nums1)+len(nums2)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        first = second = 0

        output = []

        while first < len(nums1) and second < len(nums2):
            if nums1[first][0] == nums2[second][0]:
                temp = [nums1[first][0], nums1[first][1]+nums2[second][1]]
                output.append(temp)
                first+=1
                second+=1
            elif nums1[first][0] < nums2[second][0]:
                output.append(nums1[first])
                first+=1
            else :
                output.append(nums2[second])
                second+=1
        output.extend(nums1[first:])
        output.extend(nums2[second:])
        return output
```