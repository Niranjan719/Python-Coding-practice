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

def findDuplicate(arr):
    seen = {}
    for i in arr:
        if seen.get(i):
            return i
        seen[i] = True
# Example usage:
arr1 = [4, 2, 1, 3, 1]
arr2 = [1, 4, 2, 2, 5, 2]
print(findDuplicate(arr1))  # Output: 1
print(findDuplicate(arr2))  # Output: 2
# Time complexity: O(n)
# Space complexity: O(n) due to the dictionary storage

# using floyd's tortoise and hare algorithm

def findDuplicateFloyd(arr):
    slow = arr[0]
    fast = arr[0]
    
    # Phase 1: Finding the intersection point
    while True:
        slow = arr[slow]  # Move slow by 1 step
        fast = arr[arr[fast]]  # Move fast by 2 steps
        if slow == fast:
            break
    
    # Phase 2: Finding the entrance to the cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow
# Example usage:
arr1 = [4, 2, 1, 3, 1]
arr2 = [1, 4, 2, 2, 5, 2]
print(findDuplicateFloyd(arr1))  # Output: 1
print(findDuplicateFloyd(arr2))  # Output: 2
# Time complexity: O(n)
# Space complexity: O(1) since we are not using any extra space apart from a few variables

def findDuplicate(arr):
  tortoise = arr[0]
  hare = arr[0]
  while True:
    tortoise = arr[tortoise]
    hare = arr[arr[hare]]
    if tortoise == hare:
      break
  tortoise = arr[0]
  while tortoise != hare:
    tortoise = arr[tortoise]
    hare = arr[hare]
  return tortoise

arr1 = [4, 2, 1, 3, 1]
arr2 = [1, 4, 2, 2, 5, 2]
print(findDuplicate(arr1))  # Output: 1
print(findDuplicate(arr2))


def find_duplicate_test(arr):
    t = arr[0] 
    h = arr[arr[0]]
    while t != h:
        t = arr[t]
        h = arr[arr[h]]
    t = 0
    while t != h:
        t = arr[t]
        h = arr[h]
    return t  # The duplicate number found

arr1 = [4, 2, 1, 3, 1]
arr2 = [1, 4, 2, 2, 5, 2]
print(find_duplicate_test(arr1))
print(find_duplicate_test(arr2))