# Tuples: ordered, immutable, allows duplicate elements
# Sys Module for getting code size ( as far as I know )
import sys
# timeit Module for getting the run time of whatever is being run
import timeit

# Gets the size of the variables or whatever is being run
tuple_test = (1,2,3,4, "Tester", True)
list_test = [1,2,3,4, "Tester", True]
print(sys.getsizeof(tuple_test), "Bytes")
print(sys.getsizeof(list_test), "Bytes")

# list timer
print(timeit. timeit(stmt="[1,2,3,4,5,6]", number=1000000))

# tuple timer
print(timeit. timeit(stmt="(1,2,3,4,5,6)", number=1000000))



mytuple1 = ("Max", 28, "boston")
print(mytuple1)

item1 = mytuple1[-1]
print(item1)

# another way to make an iterrable tuple as a list
mytuple2 = tuple(["Max", 28, "boston"])
print(mytuple2)

item2 = mytuple2[1]
print(item2)

# for loops
for i in mytuple2:
    print(i)

# If Statements using Tuple
if "Max" in mytuple2:
    print("yes")
else:
    print("No")
    
    
my_tuple3 = ('a', 'a', 'b', 'c', 'd', 'e', 'f')

print(len(my_tuple3))

print((my_tuple3.count('a')))

print((my_tuple3.index('a')))

# Convert Tuple to List
my_list = list(my_tuple3)
print(my_list)

# Convert List to Tuple
my_tuple4 = tuple(my_list)
print(my_tuple4)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# tuple reversal
b = a[::-1]
print(b)


# unpacking tuples
my_tuple6 = "Max", 28, "Boston"

name, age, city = my_tuple6
print(name)
print(age)
print(city)

# unpacking multiple elements in a tuple using the *
ads = (0, 1, 2, 3, 4)
i1, *i2, i3 = ads
print(i1)
print(i2)
print(i3)
