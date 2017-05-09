n = int(input("enter the number : "))

# Only divisible by itself or 1

if n>1 :
    for i in range(2,n):
        print (i)
        if n%i==0 :
            print("not a prime")
            break
        else:
            print("prime")
            break


