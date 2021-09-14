def primeornot(a):
    if a > 1:
        for j in range(2,int(a/2)+1):
            if(a % j)==0:
                print (a, "is not prime")
                break
        else:
            print(a, "is prime")
    else:
        print(a, "is not prime")
a = int(input("enter a number: "))
primeornot(a)