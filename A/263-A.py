arr = []
for _ in range(5):
    x = list(map(int, input().split()))
    arr.append(x)
    row = 0
    col = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:   
            row = i + 1 
            col = j + 1
            break

n = abs(3-row) 
m = abs(3-col)

print(n + m)
