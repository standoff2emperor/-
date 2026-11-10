a=[29,10,14,37,13]
c=[]
b=len(a)
while b > 0:
    min = a[0]
for i in range(0,b):
    if a[i]<min:
        min=a[i]
    c.append(min)
    a.remove(min)
    print(c)