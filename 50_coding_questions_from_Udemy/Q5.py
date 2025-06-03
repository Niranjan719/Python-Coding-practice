"""
Given a non-empty array of integers arr, create a function that returns the sum of the subarray that has the greatest sum.
We don't consider the empty array [] as a subarray.

Example 1:

Input: arr = [2, 3, -6, 4, 2, -8, 3]

Output: 6

Explanation: the maximum subarray is [4, 2], its sum is 6

Example 2:

Input: arr = [2, 3, -1, 4, -10, 2, 5]

Output: 8

Explanation: the maximum subarray is [2, 3, -1, 4], its sum is 8

Example 3:

Input: arr = [-3, -1, -2]

Output: -1

Explanation: the maximum subarray is [-1], its sum is -1


"""

# Brute force approach:

def maxSubArraySum(arr):
    max_sum = arr[0]
    n = len(arr)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum
# Example usage:
arr1 = [2, 3, -6, 4, 2, -8, 3]
arr2 = [2, 3, -1, 4, -10, 2, 5]
arr3 = [-3, -1, -2]
print(maxSubArraySum(arr1))  # Output: 6, subarray [4, 2]
print(maxSubArraySum(arr2))  # Output: 8, subarray [2, 3, -1, 4]
print(maxSubArraySum(arr3))  # Output: -1, subarray [-1]
# This function calculates the maximum subarray sum using a brute force approach.
# Time complexity: O(n^2)
# Space complexity: O(1) since we are using a constant amount of space for variables

# Optimized approach using Kadane's algorithm:
def maxSubArraySumKadane(arr):
    max_sum = current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
        
    return max_sum
# Example usage:
arr1 = [2, 3, -6, 4, 2, -8, 3]
arr2 = [2, 3, -1, 4, -10, 2, 5]
arr3 = [-3, -1, -2]
print(maxSubArraySumKadane(arr1))  # Output: 6, subarray [4, 2]
print(maxSubArraySumKadane(arr2))  # Output: 8, subarray [2, 3, -1, 4]
print(maxSubArraySumKadane(arr3))  # Output: -1, subarray [-1]
# This function calculates the maximum subarray sum using Kadane's algorithm.
# Time complexity: O(n)
# Space complexity: O(1) since we are using a constant amount of space for variables

# Understanding Kadane's algorithm:
# Kadane's algorithm works by iterating through the array and maintaining two variables:
# 1. `current_sum`: This keeps track of the maximum sum of the subarray ending at the current index.
# 2. `max_sum`: This keeps track of the overall maximum sum found so far.
# At each step, we decide whether to add the current element to the existing subarray (`current_sum + arr[i]`) or start a new subarray with just the current element (`arr[i]`). We then update `max_sum` if `current_sum` exceeds it.
# This approach ensures that we only traverse the array once, making it efficient for large datasets.