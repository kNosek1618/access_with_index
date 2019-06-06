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


