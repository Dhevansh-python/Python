list1=[1, 2, 3, 4, 5, 6, 7, 8]
sum=0

for i in list1:
    sum+=i

avg=sum/len(list1)

print("sum= ", sum)
print("average= ", avg)

list1.sort()

print("smallest element is ", list1[0])
print("Biggest element is ", list1[-1])