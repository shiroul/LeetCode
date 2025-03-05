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