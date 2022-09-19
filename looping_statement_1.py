
# loops in python
# range function in python
# print(f"The range from 1 to 10 is: {range(1,10+1)}")

#listing objects
from calendar import SUNDAY, THURSDAY, TUESDAY, WEDNESDAY

num_list=[]

week_days_list = [
    "SUNDAY ",
    "Monday ",
    "TUESDAY ",
    "WEDNESDAY ",
    "THURSDAY ",
    "Friday ",
    "Saturday",]
for num in range(1,11):
    print(f"The number in range is:{num}")
num_list.append(num)
print(num_list)

counter = 0
for day in week_days_list:
    counter += 1
    print(f"The {counter} day is: {day}")

    # same program with the help of range function
    for position in range(0,len(week_days_list)):
        print(f"The {position+1} position in day is: {week_days_list[position]}")

        #enumerate function
        for position,day in enumerate(week_days_list):
            print(f"The {position+1} day is: {day}")
odd_list = []
even_list = []
def filter_odd_even():
    for num in range(1,filter_odd_even+1):
        if num %2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
number = int(input("Enter any number"))
filter_odd_even(number)

print(f"Now, the odd list is:{odd_list}")
print(f"Now, the even list is:{even_list}")

[even_list.append(num) if num%2 == 0 else odd_list.append(num)]
# sth if condition else sth

