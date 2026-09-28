a=input("Enter your name: ")
b=int(input("Enter your age: "))
c=int(input("Enter your favorite number: "))
d=b+10
e=c**2
if c%2==0:
    f="even"
else:
    f="odd"
print(f"Hi {a}! In 10 years you'll be {d}. Your favorite number squared is {e}, and it's {f}.")
# It is related to the logic of input() function, so input() function recognizes every input as a string regardless it is int, str, list, boolean, or etc. And if we want to make some calculations we need to change the string type to the integer type, because python cannot do math in a string type. For this reason, we use int() function.