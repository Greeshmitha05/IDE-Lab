def countofprime(n):
    for i in range(2,n+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break;
            else:
                print(f"Prime Numbers Are {i}")

n =int(input("Enter any number: "))
countofprime(n)