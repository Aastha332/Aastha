import flask
age = int(input("Enter your age"))
if 0<age<= 10:    #age is greater than 0 and less than 10
    print(f"You are {age} years old which is less than 10 and greater than 0 so your movie ticket is Rs 100")
elif 10 <age <=20:
    print(f"You are {age} years old which is greater than 10 and less than 20 so your movie ticket is Rs 200")
elif 20<age<59:
    print(f"You are {age} years old which is greater than 20 and less than 59 so your movie ticket is Rs 200")
else:
    print(f"You are {age} years old so your movie ticket is free")

    # Note: There shouldn't be space between code line and if,elif and else and there must be space between if's print and code line otherwise it will throw error