numbers = [1, 2, 3, 4, 5, 6]
# print(numbers[0])

# print(sum(numbers))
# result = 0
# for n in numbers:
#     result += n

# print(result)


numbers = [[1, 2], [3, 4], [5, 6]]
# print(numbers[0])

# print(numbers[0][0])
# print(numbers[0][1])

# print(numbers[1][0])
# print(numbers[1][1])

# print(numbers[2][0])
# print(numbers[2][1])


# numbers = [[1,2],[3,4],[5,6]]
# result = 0
# for n in numbers:
#     result += n[0] + n[1]

# print(result)


numbers = [ [1,2,6,3] , [3,4,12,44] , [5,6,67,89] ]
res = 0
for i in range(len(numbers)):  #     i = 1       j = 2       numbers[0] = [1,2,6,3]         res = 19
    for j in range(len(numbers[i])):
        res += numbers[i][j]

print(res)


# numbers = []
# تعدادی عدد از ورودی بگیر و به لیست بالا اضافه کن
# با کمک حلقه فور و وایل مجموع اعداد رو حساب
numbers = []
for i in range(3):
    number = int(input('enter a number'))
    numbers.append(number)

print(numbers)

res = 0
for i in range(len(numbers)):
    res += numbers[i]

print(res)


numbers = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]
# با کمک دو حلقه تک تک کاراکترها را پرینت
