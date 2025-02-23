sumOfEvents = 0
arr = [0,1,2,3,4,5,6,7,8,9]
arr2 = []
for i in range(len(arr)):
    if(i % 2 != 0):
        arr2.append(-1)
    else:
        arr2.append(i)
arr2 = [[arr2[i], arr2[i + 1]] for i in range(0,len(arr2), 2)]
print(arr)
print(arr2)



