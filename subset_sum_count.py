def func(arr,i,total,dic):
    key = str(total)+'+'+str(i)
    if key in dic.keys():
        return dic[key]
    elif total==0:
        return 1
    elif i<0:
        return 0
    elif arr[i]>total:
        temp =  func(arr,i-1,total,dic)
    else:
        temp = func(arr,i-1,total-arr[i],dic)+func(arr,i-1,total,dic)
    dic[key] = temp
    return temp
dic = {}
arr = list(map(int,input().strip().split()))
total = int(input())
print(func(arr,len(arr)-1,total,dic))