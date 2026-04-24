#Question 1: Using a for loop with a list

fruits =  ["Apple", "Banana", "Orange", "Mango"]


for fruit in fruits:
  print(fruit)


print("###############################################################################################")



#Question 2: using a while loop for a countdown
#Counts in a decenting order


count = 5

while count >= 1:
  print(count)
  count -= 1



print("###############################################################################################")



#Question 3: Using a for loop with range()
#Goes through the 2 times tables counting till 11 numbers

for i in range(1, 11):
  print(i + i)




print("###############################################################################################")


#Question 4:  Using the random module
#Picks a random one from the list

import random

colours = ["Red", "orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

for i in range(3):
  print(random.choice(colours))


print("###############################################################################################")


#QUestion 5: Using custom module and calc


import math_operations
#This is the file that I made with all the calculations

while True:
  print("\nSimple Calculator")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = input("Choose an option (1-5): ")

  if choice == "5":
    print("Goodbye!!")
    break

#I'm using float instead of int, just in case division or multiplication has remainders

  num1 = float(input("Enter first number: "))
  

  num2 = float(input("Enter second number: "))

  if choice == "1":
    print("Result:", math_operations.add(num1, num2))
  
  elif choice == "2":
    print("Result:", math_operations.subtract(num1, num2))

  elif choice == "3":
    print("Result:", math_operations.multiply(num1, num2))

  elif choice == "4":
    print("Result:", math_operations.divide(num1, num2))

  else:
    print("Invalid Chioice")


