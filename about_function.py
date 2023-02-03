# define a function تعریف تابع
def calc(number1, number2):  # پارامتر ها: number1 , number2
    print(number1*2 + number2**2)


# calling th function صدازدن تابع
# calc(1, 2)
# calc(11, 2)
# calc(13, 4)
# calc(0, 4)
# print(calc(0, 3))
# x = calc(0, 3)
# print(x)

# def calc(number1, number2):  # پارامتر ها: number1 , number2
#     return number1*2 + number2**2


# x = calc(0, 3)
# print(x)


'''
Exercise1 :
یک تابعبنویسید که نمرات دروس پایتون، اسکرچ و جاوای یک دانش آموز را به همراه اسمش دریافت نماید و
معدل دانش آموز را محاسبه نماید
در نهایت پیغامی شامل نام و معدل دانش آموز نمایش دهد.
message = reza's average is 19
تا دو رقم بعد از اعشار مجاز است.

student's grade: 
A : ave >= 19  
B : ave >= 18
C : ave >= 17    
D : ave >= 16      
E : ave >= 15     
F  else
message = reza's grade is A or B or ...

'''


'''
Exercise 2 :
قرار است سفری از تهران به مشهد داشته باشید. با کمک تابع برنامه ای بنویسید که هزینه بنزین مصرفی یعنی رفت و برگشت 
را محاسبه نماید.
ورودی برنامه میزان مصرف خودرو
خروجی برنامه هزینه بنزین مصرفی در رفت و برگشت
مسافت از تهران به مشهد 1000 کیلومتر فرض شده است.
قیمت بنزین بازای هرلیتر به شرح زیر محاسبه می شود:
تا 60 لیتر، لیتری 1500
از 60 لیتر بیشتر، لیتری 3000 در نظر گرفته می شود.
'''

DISTANCE = 2000

consumption = float(input("enter your cars's consuption:> "))


def calc_litr(consumption: float, distance: float) -> float:
    '''
    This function is used to calculate amounts of litr that a car uses
    Parameters: float, consumption
    Returns : float
    '''
    return distance * consumption / 100


def calc_cost(litr: float) -> float:
    '''
    This function is used to calculate the cost of our trip.
    Parameters: float, litr
    Returns : float
    '''
    if litr <= 60:
        return litr * 1500
    return (60*1500) + (litr - 60)*3000


litr_result = calc_litr(consumption, DISTANCE)
total_cost = calc_cost(litr_result)

print(f"our trip's cost from tehran to mashhad is : {total_cost}")
