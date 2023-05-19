names = ['reza', 'artin', 'sara', 'armin', 'sara', 'rozha', 'nima', 'nikan']

# write a function that takes names as a parameter and return False if
# one or more names occured more than once
# else return True
# ارگر اسم تکراری وجو دارد
# False
# در غیر اینصورت
# True

names = ['reza', 'artin', 'sara']
# def is_unique(names_list):
#     for i in range(len(names_list)):
#         if names_list[i] in names_list[i+1:]:
#             return False
#     return True


# print(is_unique(names))

names = ['reza', 'artin', 'sara', 'armin', 'sara', 'rozha', 'nima', 'nikan']


def is_unique(names_list):
    for i in range(len(names_list)):  # 0 - 6
        for j in range(i+1, len(names_list)):
            if names_list[i] == names_list[j]:
                return (i, j, names_list[i], False)
    return True


print(is_unique(names))
