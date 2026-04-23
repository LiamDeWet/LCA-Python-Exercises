#Question 1: Basic Function


#Define the func
def greet():
  print("Hello There Liam")

#call the func
greet()

print("####################################################################################################")


#Question 2: Function with parameters

def param_greeting(name):
  print("Hello " + name + "!")

#call the func

param_greeting("Liam, nice to meet you!")

print("####################################################################################################")

#Question 3: Functions with return value

#Define
def square(number):
  return number * number


#call the func

result = square(5)
print("Square of 5 is:", result)



print("####################################################################################################")


#Question 4: Function with multiple params and return val

#Define func
def rectangle_area(length, width):
  return length * width

#call func

area = rectangle_area(4, 5)
print("Rectangle area is:", area)

print("####################################################################################################")


#Question 5: using a function as an argument


#A function that takes another function
def apply_operation(func, number):
  return func(number)

#Func to double a number
def double(number):
  return number * 2

#Use the other func with double
result1 = apply_operation(double, 7)
print("Double of 7 is:", result1)

result2 = apply_operation(square, 3)
print("Square of 3 is:", result2)