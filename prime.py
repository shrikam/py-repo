n = int(input("enter the number : "))

# Only divisible by itself or 1

if n>1 :
    for i in range(2,n):
      #  print (i)
        if n%i==0 :
            print(i)
            print("not a prime")
            break
        if i==(n-1) :
            print("prime")

