# Generate Fibonacci series up to n terms.

n = int(input("Enter a number: "))

a ,b = 0, 1
count = 0

# loop for n number of fabonacci sequence
while count < n:
    print(a, end=" ") #end=" " means end on the same line with a space
    a ,b = b , a+b
    # increment of counter value
    count +=1

