#In python function is created by using def keyword
def my_function():
    print("Hello!!!")

my_function()

#Passing parameters into function
def my_function(fname):
    print(fname+" Bulsara")

my_function("Alia")
my_function("Nushrat")
my_function("Dhvani")

#Default parameter value
def my_function(country="India"):
    print("I am from "+ country )
my_function("Sweden")
my_function()
my_function("Brazil")

#Passing a List as a Parameter
def my_function(food):
    for x in food:
        print(x)
    
food=["apple", "banana", "cherry"]
my_function(food)

#Return Values
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(4))
print(my_function(7))

#Keyword Arguments
def my_function(child1, child2, child3):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If the number of arguments are unknown, add a * before the parameter name
def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

#Recursion Example
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
