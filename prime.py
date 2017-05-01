n = int(input("entire the number : "))

# divisible by itself or 1

if n>1 :
    for i in range(2,n):
        if n%i==0 :
            print("not a prime")
            break
        else:
            print("prime")
            break


