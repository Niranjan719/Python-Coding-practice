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

# Approach 1: Using a set (Optimal - O(n) time, O(n) space)
def removeDuplicates_set(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return list(set(arr))

# Approach 2: Using a set with order preservation
def removeDuplicates_ordered(arr):
    """
    Maintains insertion order while removing duplicates.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Approach 3: Using a dictionary (preserves order in Python 3.7+)
def removeDuplicates_dict(arr):
    """
    Uses dictionary keys to remove duplicates while preserving insertion order.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return list(dict.fromkeys(arr))

# Approach 4: Sorted approach (if you want sorted output)
def removeDuplicates_sorted(arr):
    """
    Returns duplicates removed and sorted.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) == 0:
        return []
    arr.sort()
    noDuplicatesArr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            noDuplicatesArr.append(arr[i])
    return noDuplicatesArr

# Test Cases:
if __name__ == "__main__":
    arr1 = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
    arr2 = [1, 1, 1, 1, 1, 1, 1, 1]
    arr3 = [4, 4, 2, 3, 2, 2, 4, 3]
    
    print("=== Approach 1: Using set() ===")
    print(f"Test 1: {removeDuplicates_set(arr1)}")
    print(f"Test 2: {removeDuplicates_set(arr2)}")
    print(f"Test 3: {removeDuplicates_set(arr3)}")
    
    print("\n=== Approach 2: Using set with order preservation ===")
    print(f"Test 1: {removeDuplicates_ordered(arr1)}")
    print(f"Test 2: {removeDuplicates_ordered(arr2)}")
    print(f"Test 3: {removeDuplicates_ordered(arr3)}")
    
    print("\n=== Approach 3: Using dict.fromkeys() ===")
    print(f"Test 1: {removeDuplicates_dict(arr1)}")
    print(f"Test 2: {removeDuplicates_dict(arr2)}")
    print(f"Test 3: {removeDuplicates_dict(arr3)}")
    
    print("\n=== Approach 4: Sorted (O(n log n)) ===")
    print(f"Test 1: {removeDuplicates_sorted(arr1)}")
    print(f"Test 2: {removeDuplicates_sorted(arr2)}")
    print(f"Test 3: {removeDuplicates_sorted(arr3)}")

    """
    COMPLEXITY ANALYSIS:
    
    Approach 1 (set):
    - Time: O(n)
    - Space: O(n)
    
    Approach 2 (set with order preservation):
    - Time: O(n)
    - Space: O(n)
    
    Approach 3 (dict.fromkeys):
    - Time: O(n)
    - Space: O(n)
    
    Approach 4 (sorted):
    - Time: O(n log n) - dominated by sorting
    - Space: O(n)
    """
