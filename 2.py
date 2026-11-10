a=[2,5,8,11,14,18,21,25,30]
b=18
first= 0
last=len(a)-1
result = -1
while first<=last:
    mid=(first + last)//2
    if a[mid]==b:
        result=mid
        break 
    elif a[mid]<b:
        first=mid+1
    else:
        last=mid-1
print(result)

