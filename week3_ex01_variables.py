##Question 1: Variable Assignment and string manipulation

#Ask user for name:

name=input("Enter your name please :")


# ask age:

age=input("Enter you age please: ")

print("Hello " + name + "! You are " + age + " years old.")


#Personal opinion using f strings are way bettr in this situation :)


#to make the code bettr to view in the terminal i added the spaces...

#Question 2: Integer operrations

print("#######################################################################")

length = int(input("Enter the length of the rectangle: "))

width = int(input("Enter the width of the rectangle: "))

#Calculate:

area = length * width

#print result:

print("The area of the recangle is:", area)

print("#######################################################################")

#Question 3: Working with floats

#ask for temp:


celsius = float(input("Enter the temperature in Celsius: "))

#Convert to fahrenheit:

far = (celsius * 9/5) + 32

#print result:

print("Temperature in Fahrenheit is:", round(far, 2))

