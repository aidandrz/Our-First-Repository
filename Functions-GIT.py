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


# 4.14.7: Print Multiple Times
# Aidan Drzewicki
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('\n''get the bread gamers', 500)



# 4.14.7: Print Multiple Times
# Aidan Drzewicki
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('\n''get the bread gamers', 500)



# 4.16.3: Enter a Number
# Aidan Drzewicki
# 2.20.19



try:
    my_number = int(input('Enter an integer: '))
    print('Your number: ' + str(my_number))

except ValueError:
    print('That was not an integer')



<<<<<<< HEAD
# 4.16.4: Enter Name and Age
# Aidan Drzewicki
# 2.20.19

name = input('What is your name: ')

age = -1

try:
    age = int(input('Enter your age: '))

except ValueError:
    print('Thats not an age')
=======
# 4.16.6: Temperature Converter
# Aidan Drzewicki
# 2.20.19

def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 +32

def fahrenheit_to_cesius(fahrenheit):
    return(fahrenheit - 32) / 1.8

try:
    c = float(input('Enter a temp in C: '))
    print('In F: ', round(celcius_to_fahrenheit(c), 2))

    f = float(input('Enter a temp in F: '))
    print('In C:', round(fahrenheit_to_cesius(f), 2))

except ValueError:
    print('Just enter a Float 4Head')
>>>>>>> Temperature-Converter
