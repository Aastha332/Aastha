int1 = int(input( "Enter integer 1 "))
int2 = int(input ("Enter integer 2 "))
# print(integer1 + integer2)

# information1,information2 = input("What is your Brand Model Name and how much does it cost ").split(",")
# print(f"Brand name is {information1} and it's cost is {information2}")

# cost = input("How much does it cost? ")
# print(f"{cost}")

#creating function or defining function
# @substraction(int1, int2) --> This fuction is used to subtract value
def addition(int1,int2):
    sum = int1+int2
    return sum

    #calling function
print(f"The sum of two numbers is: {addition(int1,int2)}")

#python 3
print("The sum return by the function is: {}".format(addition(int1,int2)))


