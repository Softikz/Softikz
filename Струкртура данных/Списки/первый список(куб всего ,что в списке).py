lst = [1,2,3,4,5]
print(len(lst))
for i in range (0,len(lst),1):
    lst[i]=lst[i]*lst[i]

print(lst)