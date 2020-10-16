cars=["bmw","mercedes","volvo"]
x= cars[0]
print(x)
y= len(cars)
print(y)
for z in cars:
    print(z)
cars.append("Honda")
for z in cars:
    print(z)

#removing items from array
cars.pop(1)
cars.remove("volvo")
for z in cars:
    print(z)