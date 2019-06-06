print("1")

#useing a list
cars = ["ferrari", "lamborghini", "McLaren"]
print (cars)

print("2")

#access with index
cars = ["ferrari", "lamborghini", "McLaren"]
print (cars[0])

print("3")

#change object in list
cars = ["ferrari", "lamborghini", "McLaren"]
cars[1] = "Aston Martin"
print (cars[1])

print("4")
#extend the list (to cars list add engine_capacity)
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
cars.extend(engine_capacity)
print (cars)

print("5")

#with .append we can add object to the list
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
cars.append("Tesla")
print (cars)

print("6")

#.insert(index, object) when insert the other
#object is push up to the list into id index
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
cars.insert(1, "Tesla")
print (cars)

print("7")

#.remove - delete the object form list
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
cars.remove("lamborghini")
print (cars)

print("8")

#.clear - cleaning the all list
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
cars.clear()
print (cars)

print("9")

#.pop - delete last object from list
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
cars.pop()
print (cars)

print("10")

#.count - show how many object is in list
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren", "McLaren"]
print (cars.count("McLaren"))

print("11")

#.sort - sorting with numbers or first letters of words
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
engine_capacity.sort()
print (engine_capacity)

print("12")

#.reverse - reverse the list
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
cars.reverse()
print (cars)

print("13")

#.copy - copy the list to second list
engine_capacity = ["2.0", "3.5", "5.0", "2.5"]
cars = ["ferrari", "lamborghini", "McLaren"]
list2 = cars.copy()
print (list2)