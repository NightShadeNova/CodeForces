n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort() 
    diff = abs(arr[0] - arr[1])
    for i in range(1, size-1):
        if abs(arr[i] - arr[i+1]) <= diff:
            diff = abs(arr[i] - arr[i+1])
    print(diff)
