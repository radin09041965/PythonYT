# nums = [5, 7, 2, 4, 7, True, '50', 6.7, [5, 7]]
# nums[0] = 25
#
# print(*nums)
# print(nums[-1][0])
#
# numbers = [5, 2, 7]
# numbers.append(100)
# numbers.insert(1, True)
# b = [5, 7, 8]
# numbers.extend(b)
# numbers.sort()
# # numbers.reverse()
# numbers.pop(-2) # удаляет последний элемент
# numbers.remove(True)
#
# print(numbers)
# print(len(numbers))
# print(numbers.count(5))
#
# for i in nums:
#     i *= 2
#     print(i)

n = int(input('Введите длину списка: '))
user_list = []
i = 0
while i < n:
    string = 'Введите число №' + str(i +1) + ': '
    user_list.append(input(string))
    i += 1

print(*user_list)
