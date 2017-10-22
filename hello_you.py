# Ask user for name
name = input("What's your name?: ")

# Ask user for age
age = input("What's your age?: ")

# Ask user for city
city = input("What city do you live in?: ")

# Ask user what they enjoy
love = input("What do you love doing?: ")

#Create Output Text
str = 'Your name is {} and you are {} years old.  You live in {} and you love {}!'
output = str.format(name, age, city, love)

#Print Output to Screen
print(output)
