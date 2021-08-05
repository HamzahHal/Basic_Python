# Sets: unordered, mutable & no duplicates

myset = set("Hellow")
print(myset)

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(3)
print(myset)


print(myset.pop())
print(myset.pop())

for x in myset:
    print(x)


if 1 in myset:
    print("ye")
else:
    print("no")


odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

# joining 2 sets together
u = odds.union(evens)
print(u)

# finding similar numbers between 2 sets
i = odds.intersection(primes)
print(i)

# finding the different between the 2 sets, basically the numbers that arent included in SetB that are in SetA
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

# returns all elements in the 2 Sets however it wont print any element which are found in both Sets
diff2 = setA.symmetric_difference(setB)
print(diff2)

# updates elements found in another set, without duplication so basically joining them together without duplicating any values
setA.update(setB)
print(setA)
# updates elements by only showing elements found in both sets
# setA.intersection_update(setB)
# print(setA)

# this updates the set but only keeps the elements found in SetA and NOT SetB
setA.difference_update(setB)
print(setA)


for i in setA:
    print(i)

# the for loop for sets only randomizes string values however , integers are printed in the order no matter the order of input into a set

new_set = {5, 1, 2, 3, 4}

for g in new_set:
    print(g)

# the for loop for sets only randomizes string values however , integers are printed in the order no matter the order of input into a set
another_set = set("HelloTester")

for x in another_set:
    print(x)
