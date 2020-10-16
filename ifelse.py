a=5
b=5
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than b")

a=30
b=20
if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")

#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement
if a>b: print("a is greater than b")

#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
a=2
b=330
print("A") if a>b else print("B")

#AND keyword
a=10
b=5
c=2
if a>b and a>c:
    print("A is greater than b and c")

#OR keyword
if a>b or c>a:
    print("At least one of the condition is true")

#NESTED IF
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")