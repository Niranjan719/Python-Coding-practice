# Q1 . You are given a list of unsorted integers. 
# Write a Python function that returns the k most frequent elements in descending order of frequency. 
# nums - [1,2,1, 2, 1, 3, 4, 5, 4, 4],  k=2

def most_frequest_nums(nums,k):
    empty_dict = {}
    for num in nums:
        empty_dict[num] = empty_dict.get(num, 0) + 1
    work_list = list(empty_dict.items())
    sorted_list = sorted(work_list, key=lambda x: x[1], reverse = True)
    answer_list = []
    for item in sorted_list[:k]:
        answer_list.append(item[0])
    return answer_list
    
list1 = [1,2,1, 2, 1, 3, 4, 5, 4, 4]
k = 2

ans = most_frequest_nums(list1,k)
print(ans)

#Q2. Given a list of integers and a target sum, 
# return all unique pairs of elements that add up to the target.
# nums = [2, 4, 3, 5, 7, 8, 1], target = 9 

def find_pairs(nums, target):
    pairs = set()
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return pairs

# Example usage:
nums = [2, 4, 3, 5, 2, 3, 4, 7, 8, 1]
target = 9  
print(find_pairs(nums, target))


#Q3. Write a function that rotates a list to the right by k steps.
# nums = [1, 2, 3, 4, 5, 6, 7], k = 3  
# Output: [5, 6, 7, 1, 2, 3, 4]
def rotate_list(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is greater than the length of the list
    print(nums[-k:])
    return nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_list = rotate_list(nums, k)
print(rotated_list)

#Q4. Given a list of integers, write a function to find the longest increasing subsequence.
def longest_increasing_subsequence(nums):
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n  # dp[i] will hold the length of the LIS ending at index i
    prev = [-1] * n  # To reconstruct the path

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the maximum length and its index
    max_length = max(dp)
    max_index = dp.index(max_length)

    # Reconstruct the longest increasing subsequence
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]

    return lis[::-1]  # Reverse to get the correct order
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(nums))


#Q5. Write a function to find the intersection of two lists.
def intersection_of_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersection_of_lists(list1, list2)
print(result)


#Q6. Given a string, 
# find the length of the longest substring without repeating characters.
# example: "abcabcbb" should return 3 for "abc".

def length_of_longest_substring(s):
    char_index_map = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3

#Q7. Write a function to check if a string is a palindrome.
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    s = ''.join(filter(str.isalnum, s))  # Remove non-alphanumeric characters
    return s == s[::-1]  # Check if the string is equal to its reverse

print(is_palindrome("Racecar"))  # Output: True

#Q8. Given a list of integers, write a function to find the maximum product of two distinct elements.
def max_product_of_two(nums):
    if len(nums) < 2:
        return None  # Not enough elements to form a product

    max1 = max(nums)
    nums.remove(max1)
    max2 = max(nums)

    return max1 * max2
nums = [3, 5, 1, 7, 9]
print(max_product_of_two(nums))  # Output: 63 (9 * 7)
