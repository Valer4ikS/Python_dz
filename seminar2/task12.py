# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y ≤ 1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3


# s = int(input('Введите сумму чисел: '))
# m = int(input('Введите произведение чисел: '))

# x = (s - int((s ** 2 - 4 * m) ** 0.5)) // 2
# y = s - x
# if x <= 1000 and y <= 1000:
#     print('Не сходится')
# print(f'числа, которые задумал Петя : {x, y}')


x = int(input('Введите сумму чисел: '))
y = int(input('Введите произведение чисел: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)