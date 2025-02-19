
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

# weight = float(input("Enter your weight: "))
# unit = input("(L)bs or (K)g: ")

# if unit.upper() == "L":
#     print(f"You are {weight * 0.45} kilos")
# if unit.upper() == "K":
#     print(f"You are {weight / 0.45} pounds")

# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'    # Change the first element
print(names)

names.insert(1, 'Joy')  # Insert at index 1 
names.remove('Mosh')    # Remove 'Mosh'
print(len(names))

for item in names:
    print(item + 'is online')
i = 0
while i < len(names):
    print(names[i])
    i = i + 1

numbers = (1,2,3)
print(numbers[0])
# numbers[0] = 10