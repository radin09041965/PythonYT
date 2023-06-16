# word = 'Itprogres, football, skate'
#
# print(word[2])
# print(len(word))
# print(word.count('p'))
# print(word.upper())
# print(word.isupper())
# print(word.islower())
# print(word.lower())
# print(word.capitalize())
# print(word.find('p'))
#
# hobby = word.split(', ')
# print(hobby[1])
#
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
#
# print(hobby)
#
# result = ', '.join(hobby)
# print(result)

# Срезы
word1 = 'Football'
list = [8, 10, 'Stroka', 5.6]
print(word1[0:4])
print(word1[4:])
print(word1[1:-1:2]) # 2 шаг
print(list)
print(list[::-1]) # перевернуть массив
print(list[::2])
