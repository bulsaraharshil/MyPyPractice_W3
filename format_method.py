age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #format() method takes the passed arguments, formats them, and places them in the string where the placeholders {}

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #ormat() method takes unlimited number of arguments, and are placed into the respective placeholders

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #use index numbers {0} to be sure the arguments are placed in the correct placeholders

