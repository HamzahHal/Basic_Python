
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

# squared values from list
xo_o = [1, 2, 3, 4, 5, 6]

#iterrate through each value and each value is equal to x , then multiple within itself
v = [x * x for x in xo_o]

print(xo_o)
print(v)

# for loop to print the same squared values inside a print
for i in range(3):
    if i in xo_o:
        print([x * x for x in xo_o])


existing = 'e'
replace = '43'
dsfsdf = 'testing'

for x in range(1):
    while existing in dsfsdf:
        for letters in dsfsdf:
            replace = dsfsdf.replace('e', '43')
            print(replace)
            break
        print('done')
        break
print(dsfsdf)

# print(dsfsdf.replace('e', 'b'))


