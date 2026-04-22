#Question 1: Mathematical operators

x= 10
y= 5

#Adding:

x += 3

#Multiply:

y *= 2

#Divide:

result = x/y

#print results:

print("Result of x divided by y is: ", result)

print("#########################################################################################")


#Question 2: Comparison and logical operators

a= 10
b= 4
c= 8

#Conditions:

cond1 = a>b
cond2 = b % 2 == 0 #This will check if    its even
cond3 = c <= a

#Last condition:
final_cond = cond1 or (cond2 and cond3)

#Print

print("Final conditions is: ", final_cond)

print("#########################################################################################")

#Question 3: Conditional statements

#Ask for score:

score= int(input("Enter your test score please (0-100): "))

#The grading system:

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D" 

else:
  grade = "F"

#Print grade:

print("Your grade is: ", grade)

print("#########################################################################################")


#Question 4: Combining Operators and Conditionals 

#Ask for numbers:

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

#Ask for operation:

operation = input("Enter the operation (+, -, *, /): ")

#Perform the operation:
if operation == "+":
  result = num1 + num2

elif operation == "-":
  result = num1 - num2

elif operation == "*":
  result = num1 * num2

elif operation == "/":
  if num2 == 0:
    print("Error: Can't divide by zero")
  else: 
    result = num1 / num2
    print("Result: ", result)

else:
  print("Invalid operation")



print("Result: ", result)