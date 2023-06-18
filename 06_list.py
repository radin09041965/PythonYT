# nums = [5, 6, 7, 9, 4, True, 'Hello', 6.7, [2, 7]]
# nums[0] = 50
# nums[5] = 1.01
#
# print(nums[-1][1])

# numbers = [5, 4, 2]
# # numbers[3] = 100
# numbers.append(100)
# numbers.insert(1, True)
# b = [1, 5, 8]
# numbers.extend(b)
# numbers.sort()
# # numbers.reverse()
# numbers.pop(-2)
# numbers.remove(True)
# # numbers.clear() # очищает список
# # print(numbers.count(5)) # считает сколько эллементов в списке
# print(len(numbers))
#
# print(numbers)

# nums = [5, 2, 7, '50', False]
# for el in nums:
#     el *= 2
#     print(el)

n = int(input('Enter length: '))
user_list = []
i = 0
while i < n:
    string = 'Enter element №' + str(i +1) + ':'
    user_list.append(input(string))
    i += 1

print(user_list)