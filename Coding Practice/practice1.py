# def most_frequest_nums(nums, k):
#     empty_dict = {}
#     for num in nums:
#         empty_dict[num] = empty_dict.get(num, 0) + 1
#     work_list = list(empty_dict.items())
#     work_list.sort(key=lambda x: x[1], reverse=True)
#     print("Frequency list (value, count):", work_list)
#     answer_list = []
#     for i in range(0,k):
#         answer_list.append(work_list[i][0])
#     return answer_list
#     # for item in work_list[:k]:
#     #     answer_list.append(item[0])
#     # return answer_list

# # Inputs
# list1 = [1, 2, 1, 2, 1, 3, 4, 5, 4, 4]
# k = 3

# # Run
# ans = most_frequest_nums(list1, k)
# print("Input:", list1)
# print("k:", k)
# print("Output:", ans)  # Expected: [1, 4]



