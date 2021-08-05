# Recursion
def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))


nterms = int(input("Enter the terms: "))  # take input from the user

if nterms <= 0:  # check if the number is valid
    print("Please enter a positive integer ")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(fib(i))

# Loop Fibonacci
# Enter number of terms needed                   #0,1,1,2,3,5....
a = int(input("Enter the terms: "))
first = 0                                         # first element of series
second = 1                                         # second element of series
if a <= 0:
    print("The requested series is", f)
else:
    print(first, second, end=" ")
    for x in range(2, a):
        Next = first + second
        print(Next, end=" ")
        first = second
        second = Next