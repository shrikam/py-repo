import random
x = random.sample(range (100),20)
y = random.sample(range (20),15)
print(x)
print(y)
a= []
for num in x:
    if num in y:
     a.append(num)
print(a)
