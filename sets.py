#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

thisset = {"apple","banana","cherry"}
print(thisset)

for x in thisset:
    print(x)

print("banana" in thisset)

thisset.update(["orange", "mango", "grapes"])
print(thisset)

thisset.remove("banana")
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


#sets, tuples and lists are almost same

