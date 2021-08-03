
num_list = [5, 6, 39, 239, 0, -1]
mylist = ['Banana'.lower(), 'Cherry', 'Apple']
print(mylist)


if 'banana'.lower() in mylist:
    print('Yes')
else:
    print('Nope')

mylist.append('Lemon')
print(mylist)

mylist.insert(0, 'Blueberry')
print(mylist)


item = mylist.pop(-1)
print(item)
print(mylist)

item = mylist.remove('banana')
print(mylist)


item2 = num_list.reverse()
print(num_list)

item3 = num_list.sort()
print(num_list)

new_list = sorted(num_list)
print(num_list)

multiple_element = [0] * 5
print(multiple_element)

mylist2 = [1, 2, 3, 4, 5]

list_times = mylist2 + multiple_element
print(list_times)

range_list = [1, 2, 3, 4, 5, 6]

a = range_list[::-1]
print(a)

range_list.reverse()
print(range_list)


list_org = ['banana', 'cherry', 'apple']

list_cpy = list_org

list_cpy.insert(0,'Cucumber')
print(list_cpy)
print(list_org)

xo_o = [1, 2, 3, 4, 5, 6]
v = [x * x for x in xo_o]

print(xo_o)
print(v)


for i in range(2):
    for x in xo_o:
        xo_o * x
        print(xo_o)
        break
