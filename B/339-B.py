n, m = input().split()
n = int(n)
m = int(m)
a =[]
a = input().split()
a = list(map(int, a))
sum = a[0] - 1
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        sum = sum + (a[i] - a[i-1])
    elif a[i] == a[i-1]:
        continue
    elif a[i] < a[i-1]:
        sum = sum + (n-a[i-1]) + (a[i])
print(sum)
