
# first = float(input("Enter first number: "))
# second = float(input("Enter second number: "))

# print("Sum of two numbers is: ", first + second)

# course = "Python for beginners"

# print(course.upper())
# print(course.lower())
# print(course.replace("r", "R"))
# print('Pytho' in course)
# print('Pytho' in course and "beginners" in course)
# print(not 'Python' in course)

# temperature = 22

# if(temperature > 30):
#     print("It's a hot day")
# elif(temperature > 20):
#     print("It's a nice day")
# else:
#     print("It's not a hot day")

weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    print(f"You are {weight * 0.45} kilos")
if unit.upper() == "K":
    print(f"You are {weight / 0.45} pounds")