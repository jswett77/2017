# Comments
# Start with a hashtag, and don't get run by the compiler
# Comments let you mark up your code to help remind you
# of how the code works

# Example of declaring a variable named message1 and assigning the string "hello from the binary"
# variables must start with letters and cannot contain any spaces
message1 = "hello from the binary"

# example of using the variable message1 to be printed to the command line
print(message1)

# example of changing the value message1 to something else
# and then printing it
message1 = "some OTHER message"
print(message1)

# Example of using "built-in" utility methods
# .upper(), .lower(), .title()
# The parenthesis are required. They tell the compiler to execute the method "upper" etc
print(message1.upper())
print(message1.lower())
print(message1.title())

# Example of printing a greeting to the console
message2 = "justin swett"
print("Hello " + message2.title())

# example of a variable that is used to hold onto a number
number = 12345
print(number)

# try uncommenting the following line:
# print("the number is: " + number)

# you can fix the problem by telling the compiler that number should be converted to a string
print("the number is: " + str(number))

# Example of embedding double quote, or single quote marks inside of a variable
message3 = 'I can "code" now'
print(message3)
message4 = "It's a bit chilly! Yoinks!"
print(message4)

print(message3 + " " + message4)

message5 = "It's not problem. \"Cool story bro\""
print(message5)



