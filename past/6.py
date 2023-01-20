# names = ('ramtin', 'rozhman', 'nikan', 'sima')

# print(names[0])
# print(names[-1])

# slice برش
# print(names[1:3])

# tuple is immutable تاپل غیرقابل تغییر است

# names[0] = "nima"  # خطا می دهد. چون تاپل قابل تغییر دادن نیست
# names.append('sssss')  # خطا
# names.remove('ramtin')  # خطا


# number = (1,)

# number1 = (1, 2)
# number2 = (3, 4)

# number = number1 + number2

# print(number)

# print((1,2)*3)


# dictionary دیکشنری
# فرض کنیم می خواهیم ورزش مورد علاقه هر دانش آموز را ذخیره نمائیم
# favorite_sports = ["football", "baseball", "basketball", "pingpong"]
# بنابراین از نوع داده لیست نمی شود استفاده

# favorite_sports = {}
# print(type(favorite_sports))

# favorite_sports = {
#     'nima': 'football',
#     'reza': 'baseball',
#     'sima': 'basketball'

# }

# print(favorite_sports)
# print("nima likes:", favorite_sports['nima'])
# print("reza likes:", favorite_sports['reza'])
# print("sima likes:", favorite_sports['sima'])

# اضافه کردن آیتم جدید به دیکشنری
# favorite_sports['nikan'] = 'skate'
# حذف کردن از داخل دیکشنری
# del favorite_sports['reza']

# print(favorite_sports)

# favorite_sports = {
#     0: 'football',
#     1: 'baseball',
#     2: 'basketball'

# }
# print(favorite_sports[0])
# print(favorite_sports[1])
# print(favorite_sports[2])


# آیا عملگر + روی دیکشنری کار می کند؟

# student1 = {
#     'id': 1,
#     'name': 'nikan',
#     'age': 22
# }
# student2 = {
#     'id': 2,
#     'name': 'vihan',
#     'age': 23
# }

# student = student1 + student2 # خطا
# print(student) # خطا

# student = student1 * 3  # خطا
# print(student)  # خطا


# excersise1:
# یک دیکشنری بساز که دارای کلید و مقادیر باشد:
# کلید ها:
# id
# name
# family
# grade
# age

# مقادیر:

# 1
# ali
# rezaei
# 90
# 15

# سپس مقدار کلید 
# grade 
# را نمایش بده


person = {
    'id':1,
    'name': "reza",
    "age":12
}

del person['age']

print(person)