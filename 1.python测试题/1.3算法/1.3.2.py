def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2) 

    if len(nums) % 2 == 0:  
        mid = len(nums) // 2
        return (nums[mid - 1] + nums[mid]) / 2  
    else:
        mid = len(nums) // 2
        return nums[mid] 

# example:
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))  # 输出: 2.00000
