n = int (input("plz enter the number : "))

factorial=1
if n<0 : print ("no factorial")
elif n==0 : print ("factorial of 0 is 1")
else:
    for i in range (1, n+1):
        factorial=factorial*i
        print(factorial)


