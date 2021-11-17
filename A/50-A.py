m, n = input().split()
m = int(m)
n = int(n)
s = m * n
if s%2 == 0:
    print (int(s/2))
else:
    print(int((s-1)/2))
