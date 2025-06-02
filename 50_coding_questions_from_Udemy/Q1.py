# These are from Udemy course.

# Q1. Given an array of integers arr and an integer k, 
# create a boolean function that checks if there exist two elements in arr such that we get k when we add them together.

# Example 1:

# Input: arr = [4, 5, 1, -3, 6], k = 11

# Output: true

# Explanation: 5 + 6 is equal to 11

# Example 2:

# Input: arr = [4, 5, 1, -3, 6], k = -2

# Output: true

# Explanation: 1 + (-3) is equal to -2

# Example 3:

# Input: arr = [4, 5, 1, -3, 6], k = 8

# Output: false

# Explanation: there is no pair that sums up to 8

# Brute force:

def has_pair_with_sum(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False
# Time complexity: O(n^2)
# Space complexity: O(1)
#===========================================

# By sorting the array:
def has_pair_with_sum(arr,k):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] == k:
            return True
        elif arr[left] + arr[right] < k:
            left += 1
        elif arr[left] + arr[right] > k:
            right -= 1
    return False
# Example usage:
arr = [4, 5, 1, -3, 6]
k = 11
print(has_pair_with_sum(arr, k))  # Output: True
# Time complexity: O(nlogn)
# Space complexity: depends on the sorting algorithm we use

#===========================================
# Use a hash set:

def has_pair_with_sum(arr, k):
    seen = set()
    for num in arr:
        complement = k - num
        if complement in seen:
            return True
        seen.add(num)
    return False
# Example usage:
arr = [4, 5, 1, -3, 6]
k = 11
print(has_pair_with_sum(arr, k))  # Output: True

# Time complexity: O(n)
# Space complexity: O(n)