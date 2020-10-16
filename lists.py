thislist = ["apple","mango","banana"]
for x in thislist:
    print(x)

if "apple" in thislist:
    print("Yes, 'apple' is in this list")

    print(len(thislist)) #length of thislist

    thislist.append("orange")
    print(thislist) #to add another item in list

    thislist.insert(1,"cherry")
    print(thislist) #insert is used to add item at particular index

    thislist.remove("cherry")
    print(thislist) #remove is used to remove particular item from list

    thislist.pop()
    print(thislist) #pop() method removes the specified index, (or the last item if index is not specified)

    del thislist[0]
    print(thislist) #del keyword removes the specified index and del without index is used to remove full list eg:-del thislist

    thislist.clear()
    print(thislist) # clear is used to remove full list


    # copy a list

    thislist = ["banana","apple","orange"]
    mylist = thislist.copy()
    print(mylist)

    #join 2 lists

    list1=["a","b","c"]
    list2=[1,2,3]
    list3=list1+list2
    print(list3)

for x in list2:
    list1.append(x) 
    print(list1)      # join two lists are by appending all the items from list2 into list1, one by one

    list1.extend(list2)
    print(list1)      #extend() method to add list2 at the end of list1

#using list() constructor to make a list

thislist = list(("cherry","pear","guava"))
print(thislist)


#lists, tuples and sets are almost same