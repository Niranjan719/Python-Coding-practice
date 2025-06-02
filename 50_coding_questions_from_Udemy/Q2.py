"""Given a string str, create a function that returns the first repeating character.
If such character doesn't exist, return the null character '\0'.

Example 1:

Input: str = "inside code"

Output: 'i'

Example 2:

Input: str = "programming"

Output: 'r'

Example 3:

Input: str = "abcd"

Output: '\0'

Example 4:

Input: str = "abba"

Output: 'b'"""

#Brute force approach:
def firstRepeatingCharacter(str):
    ll1 = list(str)
    for i in range(len(ll1)):
        for j in range(i):
            if ll1[i] == ll1[j]:
                return ll1[i]
    return '\0'  # Return null character if no repeating character is found

str = "inside code"
print(firstRepeatingCharacter(str))  # Output: 'i'

#=============================================

# Using a set to track seen characters:

def firstRepeatingCharacter(str):
    seen = set()
    for char in str:
        if char in seen:
            return char
        seen.add(char)
    return '\0'  # Return null character if no repeating character is found

"""
Complexity analysis
Solution 1:

We put n = length of str

Time complexity: O(n²)

Explanation:

The outer loop is repeated n times, the inner loop is repeated i times, and what's inside the inner loop costs O(1) because we just compare characters and eventually return a character

Cost of iterations of the outer loop:

1st iteration -> i = 0

2nd iteration -> i = 1

3rd iteration -> i = 2

.

.

nth iteration -> i = n-1

The sum is 0+1+2+...+(n-1), it's the sum of integers from 0 to n-1, which is equal to n(n-1)/2

T(n) = n(n-1)/2 = (n²-n)/2 = n²/2 - n/2, we take the greatest term, we remove the constant, and we get a time complexity of O(n²)

Space complexity: O(1)

Explanation:

We're just using two integer variables i and j, the extra space is 2, it's a constant

S(n) = 2 = O(1)



Solution 2:

We put n = length of str

Explanation:

The loop is traversing characters of str, so it does n iterations, and at each iteration, we are searching for a key in the hash table and eventually inserting a value. And in a hash table, inserting, searching, and removing have an O(1) cost in average, so:

T(n) = n*O(1) = O(n)

Space complexity: O(n)

Explanation:

In the worst case, every character needs to be inserted in the hash table, this case happens when each character is unique and we don't find a repeating character. And we have n characters, the extra space would be n, so:

S(n) = O(n)



Note that we can also use a set instead of a hash table, we get the same time and space complexity

"""