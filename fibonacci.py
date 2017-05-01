n = int(input("enter the number   "))
def Fib(n):
   # print("entered number is :")
    if n==0: return 0
    if n==1: return 1
    else: return (Fib(n-1)+Fib(n-2))
a= 0
while(a<=n):
 print (Fib(a))
 a=a+1