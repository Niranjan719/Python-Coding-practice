"""
Given an array of integers arr that contains n+1 elements between 1 and n inclusive, create a function that returns the duplicate element (the element that appears more than once). Assume that:
- There is only one duplicate number
- The duplicate number can be repeated more than once

Example 1:

Input: arr = [4, 2, 1, 3, 1]

Output: 1

Example 2:

Input: arr = [1, 4, 2, 2, 5, 2]

Output: 2

"""

# My Solution:

def findDuplicate(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]
    return None  # If no duplicate is found
# Example usage:
arr1 = [4, 2, 1, 3, 1]
arr2 = [1, 4, 2, 2, 5, 2]
print(findDuplicate(arr1))  # Output: 1
print(findDuplicate(arr2))  # Output: 2
# Time complexity: O(n log n) due to sorting
# Space complexity: O(1) if we ignore the input array storage


# Alternative Solution using a set:
def findDuplicateSet(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None  # If no duplicate is found
# Example usage:
arr1 = [4, 2, 1, 3, 1]
arr2 = [1, 4, 2, 2, 5, 2]
print(findDuplicateSet(arr1))  # Output: 1
print(findDuplicateSet(arr2))  # Output: 2
# Time complexity: O(n)
# Space complexity: O(n) due to the set storage