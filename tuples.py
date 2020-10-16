#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets

thistuple = ("cherry","banana","apple")
print(thistuple) 

print(thistuple[1])

print(thistuple[-1])

#change tuple values

y = list(thistuple)
y[1] = "kiwi"
print(y)

for x in thistuple:
    print(x)
    

#tuples, sets and lists are almost same