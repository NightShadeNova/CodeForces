import math
n, m, a = map(float, input().split())
x = math.ceil(n/a)
y = math.ceil(m/a)
 
print(int(x*y))
