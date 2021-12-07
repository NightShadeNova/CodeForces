n = int(input())
arr_x = []
arr_y = []
arr_z = []
for i in range(n):
    x, y, z = input().split()
    arr_x.append(int(x))
    arr_y.append(int(y))
    arr_z.append(int(z))
if sum(arr_x) == 0 and sum(arr_y) == 0 and sum(arr_z) == 0:
    print("YES")
else:
    print("NO")
