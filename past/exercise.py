'''
* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *
'''
# for row in range(10):
#     print('*', end=" ")
# print()
# for row in range(5):
#     print('*', end=" ")
# print()
# for row in range(20):
#     print('*', end=" ")

# print("* "* 10)
# print("* "* 5)
# print("* "* 20)


'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
# for row in range(10):
#     for col in range(10):
#         print("*", end=" ")
#     print()


'''
* * * *
* * * *
* * * *
* * * *
* * * *
* * * *
* * * *
* * * *
* * * *
* * * *


'''
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *


'''
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
'''

'''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5



9  
'''
'''
0
0 1
0 1 2
0 1 2 3 
0 1 2 3 4
0 1 2 3 4 5 

                  9


'''
'''
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
            

                  0
'''

# import time
# for row in range(10):
#     for j in range(row):
#         print(" ", end=" ")
#     for j in range(10-row):
#         print(j, end=" ")
#     print()


'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 
0 1 2 3 4 5 6 7 
0 1 2 3 4 5 6 
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 
0 




'''

'''
1  2  3  4  5  6  7  8  9
2  4  6  8 10 12 14 16 18
3                       27
4                        36


9                         81



'''
# 
# t1 = time.time()
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i*j < 10:
#             print(" ", end="")
#         print(i*j, end='    ')
#     print()
# t2 = time.time()
# print("first experiment result")
# print(t2-t1)
####################################################
# t1 = time.time()
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(str(i*j).rjust(4), end=" ")
#     print()
# t2 = time.time()
# print("second experiment result")
# print(t2-t1)

