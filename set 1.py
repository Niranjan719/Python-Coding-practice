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

ans = most_frequest_words(list1,k)
print(ans)


