# name = input("Enter your name ")
# print(f"Hi {name} Nice to meet you")

# information1,information2 = input("What is your Brand Model Name and how much does it cost ").split(",")
# print(f"{information1} {information2}")
# information2 = type(information2)

brand_name, model_name, price = input("Enter your laptop details (brand_name, model_name, price)").split(",")

def laptop(brand_name, model_name, price):
    return f"{brand_name} {model_name} {price}"

print(laptop(brand_name, model_name, price))

