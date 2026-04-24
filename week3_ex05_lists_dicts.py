#Question 1: Creating and modifying lists


#Create the list

fruits = ["Apple", "Orange", "Pear", "Peach"]

print("Original fruits list: ", fruits)

#Adding a fruit
fruits.append("Plum")

#Insert a fruit st the beginning
fruits.insert(0, "Grapes")

#Remove a fruit
fruits.remove("Orange")

#Print result
print("Modified fruits list: ", fruits)

#I literally have no idea hwy i kept using print() with a bunch of hashtags in it when i could have just done this, lol ;)

print("\n" * 2)


#Question 2: List Operations

#Create list 1-5

numbers = [1,2,3,4,5]

#Square each of them

squared_numbs = []
for num in numbers:
  squared_numbs.append(num ** 2) #easy math, not sure if ^ works??

#Sum and Average

total = sum(numbers)
average = total / len(numbers)


#Print results

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbs)
print("Sum:", total)
print("Average:", average)

print("\n" * 2)

#Question 3: Creating and modifying dictionaries
#Create the dictionary

countires = {
  "South Africa": "Pretoria",
  "USA": "Washington D.C",
  "France": "Paris"
}

#Show the original
print("Original list from countires", countires)

print("\n" * 2)

#Add a new pair

countires["Germany"] = "Berlin"

#Update existing

countires["USA"] = "Washington, D.C."

#Remove a pair

countires.pop("France")

#print results

print("Modified countires dictionary:", countires)


print("\n" * 2)

#Question 4: Dictionary operations

fruit_colours = {
  "Apple": "Red",
  "Banana": "Yellow",
  "Plum": "Purple"

}

#Print keys
print("Fruits:", list(fruit_colours.keys()))

#Print values

print("Colours:", list(fruit_colours.values()))

#print each fruit and colour

for fruit, colour in fruit_colours.items():
  print(fruit, "is", colour)

#Check if fruit exists

check_fruit = input("Enter a fruit to check: ")

if check_fruit in fruit_colours:
  print(check_fruit, "is", fruit_colours[check_fruit])

else:
  print("Fruit not found")



