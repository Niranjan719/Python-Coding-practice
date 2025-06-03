"""
Given an array of integers arr, create a function that returns an array containing the values of arr without duplicates (the order doesn't matter).

Example 1:

Input: arr = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]

Output: [4, 2, 5, 3, 1]

Example 2:

Input: arr = [1, 1, 1, 1, 1, 1, 1, 1]

Output: [1]

Example 3:

Input: arr = [4, 4, 2, 3, 2, 2, 4, 3]

Output: [4, 2, 3]
"""
# def removeDuplicates(arr):
#   if len(arr) == 0:
#     return []
#   arr.sort()
#   noDuplicatesArr = [arr[0]]
#   for i in range(1, len(arr)):
#     if arr[i] != arr[i-1]:
#       noDuplicatesArr.append(arr[i])
#   return noDuplicatesArr

# print(removeDuplicates([4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]))  # Output: [1, 2, 3, 4, 5]




def remove_duplicates(arr):
    seen= set()
    result = []

    for num in arr:
        if num in seen:
            continue
        seen.add(num)
        result.append(num)
    return result

print(remove_duplicates([4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1,100]))

def removeDuplicates(arr):
    # your code here
    ans = set(arr)
    return list(ans)

# Example usage:
arr1 = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
arr2 = [1, 1, 1, 1, 1, 1, 1, 1]
arr3 = [4, 4, 2, 3, 2, 2, 4, 3]
print(removeDuplicates(arr1))  # Output: [1, 2, 3, 4, 5]
print(removeDuplicates(arr2))  # Output: [1]
print(removeDuplicates(arr3))  # Output: [2, 3, 4]


def removeDuplicates(arr):
    visited = {}
    for i in arr:
        visited[i] = True
    return list(visited.keys())
# Example usage:
# arr1 = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
# arr2 = [1, 1, 1, 1, 1, 1, 1, 1]
# arr3 = [4, 4, 2, 3, 2, 2, 4, 3]
# print(removeDuplicates(arr1))  # Output: [4, 2, 5, 3, 1]
# # print(removeDuplicates(arr2))  # Output: [1]
# # print(removeDuplicates(arr3))  # Output: [4, 2, 3]


def removeDuplicates(arr):
  visited = set()
  for element in arr:
    visited.add(element)
  return list(visited)
# Example usage:
# arr1 = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
# arr2 = [1, 1, 1, 1, 1, 1, 1, 1]
# arr3 = [4, 4, 2, 3, 2, 2, 4, 3]
# print(removeDuplicates(arr1))  # Output: [4, 2, 5, 3, 1]
# print(removeDuplicates(arr2))  # Output: [1]
# print(removeDuplicates(arr3))  # Output: [4, 2, 3]


"""
Complexity analysis
Solution 1:

We put n = length of arr

Time complexity: O(n²)

Explanation:

The loop is traversing elements of arr, so it does n iterations, and at each iteration, we are checking if the element is not in noDuplicatesArr. And searching for an element in an unsorted array has an O(n) cost where n is the number of elements in it

Cost of searching for the element in noDuplicatesArr:

1st iteration: noDuplicatesArr has 0 elements -> cost: 0

2nd iteration: noDuplicatesArr has 1 element -> cost: 1

3rd iteration: noDuplicatesArr has 2 elements -> cost: 2

.

.

nth iteration: noDuplicatesArr has n-1 elements -> cost: n-1

The sum is 0+1+2+...+(n-1), it's the sum of integers from 0 to n-1, which is equal to n(n-1)/2

T(n) = n(n-1)/2 = (n²-n)/2 = n²/2 - n/2, we take the greatest term, we remove the constant, and we get a time complexity of O(n²)

Space complexity: O(n)

Explanation:

We're using an extra array that will contain n elements in the worst case, when there are no duplicates in arr, so:

S(n) = O(n)



Solution 2:

We put n = length of arr

Time complexity: O(nlogn)

Explanation:

Sorting the array costs nlogn

The for loop does n-1 iterations because i starts at 1 and stops when it reaches n. And at each iteration, we are comparing 2 integers, O(1) cost, and appending an integer, O(1) amortized cost, so the cost of an iteration is O(1)

T(n) = nlogn + n-1 = O(nlogn)

Space complexity: O(n)

Explanation:

We are using extra space for the noDuplicatesArr that can contain n elements in the worst case, so:

S(n) = O(n)



Solution 3:

We put n = length of arr

Time complexity: O(n)

Explanation:

Inserting an element in a hash table costs O(1) in average, and we are doing it for each element

We also have the cost of converting the keys of the hash table into an array, which is n

T(n) = n+n = 2n = O(n)

Space complexity: O(n)

Explanation:

The hash table can contain n elements in the worst case, when there are no duplicates, so:

S(n) = O(n)



Note that we can also use a set instead of a hash table, we get the same time and space complexity


"""
