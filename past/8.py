"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
# print(' '*4 + '* '*1)
# print(' '*3 + '* '*2)
# print(' '*2 + '* '*3)
# print(' '*1 + '* '*4)
# print(' '*0 + '* '*5)

# for i in range(5):
#     print(' '*(5-i-1) + '* '*(i+1))

'''
* * * * * 
 * * * * 
  * * * 
   * * 
    *





'''


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
for i in range(9):
    if i <= 9/2:
        print('* ' * (i+1))
    else:
        print('* ' * (9-i))


        
n = int(input('enter how many stars do you want? '))
for i in range(n):
    if i <= n/2:
        print('* ' * (i+1))
    else:
        print('* ' * (n-i))
