nums1 = [2,0]
m = 1
nums2 = [1]
n = 1



i = m - 1  # Pointer for nums1
j = n - 1  # Pointer for nums2
k = m + n - 1  # Pointer for the final position in nums1

# Merge nums1 and nums2 from the end
while j >= 0:
    if i >= 0 and nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1
            

print(nums1)
