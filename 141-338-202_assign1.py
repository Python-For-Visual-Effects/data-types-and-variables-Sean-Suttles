"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.

# 3.- Make a program that prints a sentence that includes at least 3 variables.

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"

#1
print(64+32)

#2
a = 1
b = 2
print(a + b)

#3
a = 1
b = 2
c = 3
print("The sum of a, b, c is ", a + b + c,".")

#4

a = "This is my first Python program."
print(len(a))

#5

y = 1920
x = 1080
var1 = (y*.1)
var2 = (x*.1)
print("The 10% overscan of 1920 is",var1, "and the 1080 is",var2,".")
