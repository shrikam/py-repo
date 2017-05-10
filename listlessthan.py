a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print (a)
l=len(a)
f=[]
j=0
for i in range(0,l):
    if a[i]< 20:
        f.append(a[i])
        j=j+1

print (f)
