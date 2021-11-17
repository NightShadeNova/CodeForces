n, k = input().split()
n = int(n)
k = int(k)
arr = list(map(int,input().split()))
i = 0
while (i< n and arr[i] >= arr[k-1] and arr[i] >0):
    i+=1
print(i)
