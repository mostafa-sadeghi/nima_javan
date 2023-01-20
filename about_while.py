# x = ['a', 1, {'id': 1}, (1, 2)]

# print(len(x))

# for item in x:
#     pass


# while loop
# this is like scratch forerver loop
# infinite loop
# while True:
#     print("ok")

# x = ['a', 1, {'id': 1}, (1, 2)]

# for item in x:
#     print(item)

# write above loop with while loop
# 1. counter
# 2. condition
# 3. update counter (counter state)

# i = 0
# while i < len(x):
#     print(x[i])
#     i += 1  # i = i+1
"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""

# i = 0
# while i < 5:
#     print(' '*(4-i) + '* '*(i+1))
#     i += 1
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    *
'''

# i = 0
# while i < 5:
#     print(' '*i + ' *'*(5-i))
#     i += 1
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
# for i in range(9):
#     if i <= 9/2:
#         print('* ' * (i+1))
#     else:
#         print('* ' * (9-i))

# i = 0

# while i < 9:
#     if i <= 9/2:
#         print('* ' * (i+1))
#     else:
#         print('* ' * (9-i))
#     i += 1


'''
     *
   * *     
 * * *
   * *
     *  

'''
# print(' '*4 + '* '*1)
# print(' '*2 + '* '*2)
# print(' '*0 + '* '*3)
# print(' '*2 + '* '*2)
# print(' '*4 + '* '*1)

# 3 2    4  4
# i = 0
# j = 1
# while i < 5:
#     if i < 5/2:
#         print(' '*(4-2*i) + '* '*(i+1))

#     else:
#         print(' '*(i-j) + '* '*(5-i))
#         j -= 1

#     i += 1

'''
        *
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *      


'''

# print(' '*8 + '* '*1)
# print(' '*6 + '* '*3)
# print(' '*4 + '* '*5)
# print(' '*2 + '* '*7)
# print(' '*0 + '* '*9)

# i = 0
# j = 5
# while i < 5:
#     print(' '*((j-1)*2) + '* '*((i*2)+1))
#     i += 1
#     j -= 1

'''
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * * 
        *
'''

# print(' '*0 + '* '*9)
# print(' '*2 + '* '*7)
# print(' '*4 + '* '*5)
# print(' '*6 + '* '*3)
# print(' '*8 + '* '*1)
# i = 0
# j = 5
# while i < 5:
#     print(' '*(i*2) + '* '*((j*2)-1))
#     i += 1
#     j -= 1

'''
    *
  * *
* * *


'''
# exercise1:
print(' '*4 + '* '*1)
print(' '*2 + '* '*2)
print(' '*0 + '* '*3)

# exercise2
'''
*
* *
* * *
* * * *
* * * * *



'''

# exercise3
'''
* * * * *
* * * *
* * *
* *
*
'''


# exercise4
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
# exercise5
'''
* * * * *
* * * * *
* * * * *
* * * * *

'''
