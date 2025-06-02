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


"""
Solution 1:

We put n = length of arr

Time complexity: O(n²)

Explanation:

The outer loop is repeated n times, the inner loop is repeated n-(i+1) times, and what's inside the inner loop costs O(1)

Cost of iterations of the outer loop:

1st iteration -> i = 0 -> n-(i+1) = n-1

2nd iteration -> i = 1 -> n-(i+1) = n-2

3rd iteration -> i = 2 -> n-(i+1) = n-3

.

.

nth iteration -> i = n-1 -> n-(i+1) = 0

So T(n) = (n-1)+(n-2)+(n-3)+...+0, which is the sum of integers from n-1 to 0, which is n(n-1)/2

T(n) = n(n-1)/2 = (n²-n)/2 = n²/2 - n/2, we take the greatest term, we remove the constant, and we get a time complexity of O(n²)

Space complexity: O(1)

Explanation:

We are using 2 integer variables i and j only, it's a constant

S(n) = 2 = O(1)



Solution 2:

We put n = length of arr

Time complexity: O(nlogn)

Explanation:

Sorting the array costs nlogn

Left and right start at the extremities of arr, and at each iteration, one of them moves by one position to the other one, so the while loop does at most n iterations before they meet, and each iteration has an O(1) cost because we just add, compare, increment, decrement, or return

T(n) = nlogn + n = O(nlogn)

Space complexity: Depends on the sorting algorithm we use

Explanation:

It's true that we're using 2 integer variables left and right only, but the extra space also depends on the sorting algorithm we used



Solution 3:

We put n = length of arr

Time complexity: O(n)

Explanation:

The loop is traversing elements of arr, so it does n iterations, and at each iteration, we are searching for a key in the hash table and eventually inserting a value. And in a hash table, inserting, searching, and removing have an O(1) cost in average, so:

T(n) = n*O(1) = O(n)

Space complexity: O(n)

Explanation:

In the worst case, every element needs to be inserted in the hash table, this case happens when each element is unique and we don't find a pair that sums up to k. And we have n elements, the extra space would be n, so:

S(n) = O(n)

Note that we can also use a set instead of a hash table, we get the same time and space complexity
"""