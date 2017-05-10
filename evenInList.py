import random
x = random.sample(range (50),10)
print (x)
f=[]
for i in range (0, len(x)):
     if (x[i]%2)==0:
        f.append(x[i])
print (f)