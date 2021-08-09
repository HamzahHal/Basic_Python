from collections import Counter

testing = 'a'
my_counter = Counter(testing)
x = 0
while x <= my_counter['a']:
    print(my_counter['a'])
    testing += 'a'
    x += 1
