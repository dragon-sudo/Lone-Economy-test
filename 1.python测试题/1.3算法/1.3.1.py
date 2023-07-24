def two_sum(nums, target):
    num_map = {}  # Create a hash map to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            # If the complement is in the hash map, return the indices of the two numbers
            return [num_map[complement], i]
        
        # If not found, add the current number to the hash map
        num_map[num] = i

    # If no valid answer exists, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
