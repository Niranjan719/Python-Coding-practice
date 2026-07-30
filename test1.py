
# Find First Non-Repeating Character
def first_unique(value):
    char_count = {}
    
    for char in value:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in value:
        if char_count[char] == 1:
            return char
    
    return None




print(first_unique("aabbcde"))