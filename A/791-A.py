m, n = map(int, input().split())
 x = 0
while m <= n:
    x += 1 
    m = 3*m
    n = 2*n
print (x)
