# Aidan Drzewicki
# 4.13.3: Greeting
# 2.6.19


name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you!")

greeting()


# 4.13.4: Functions and Variables
# Aidan Drzewicki
# 2.14.19

x = 11

def print_something():
    x = 13
    print(x)

print_something()
print(x)



# 4.13.5: Functions & Variables - Part 2
# Aidan Drzewicki
# 2.14.19

my_variable = 3.6745

def something():
    print(my_variable + 10)

    something()


# 4,13,6: Functions and Variables, Part 3
# Aidan Drzewicki
# 2/18/19

def print_number(x):
    print(str(x))

print_number(12)
print_number('\n'"Hello World")


# 4.14.4; Name & Age
# Aidan Drzewicki
# 2.18.19

def name_and_age(name, age):
    print('\n'"Hi, my name is", name, 'and I am', str(age), 'years old.')

name_and_age('Aidan Drzewicki', 15)
name_and_age('Gamer', 1)
name_and_age('E', 63)


# 4.13.5: Default Parameter Values
# Aidan Drzewicki
# 2.19.19


def print_two_numbers(x, y = 20):
    print('First number:', str(x))
    print('Second number:', str(y))

print_two_numbers(5, 69)
print_two_numbers(23)