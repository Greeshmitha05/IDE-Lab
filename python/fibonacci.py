def fibonacci(x):
    first,second=0,1
    count=0
    if x<=0:
        print("Enter any number")
    elif x==1:
        print(f"Fibonacci sequence upto {x} are {first}")
    else:
        print("Fibnonacci Sequence:")
        while count<x:
            print(first)
            last=first+second
            first=second
            second=last
            count+=1

x=int(input("Enter the no of Fibonacci Sqeuences to be printed: "))
fibonacci(x)