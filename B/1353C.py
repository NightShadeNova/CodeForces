a = int(input())
for i in range(a):
    n = int(input())
    x = (2*n) + 2*(n-2)
    sum = 0
    for k in range(1, n+1, 2):
        #number of squares in the the outermost ring
        x = (2*k) + 2*(k-2)
        #number of steps for each square to get to middle 
        y = (k-1)//2
        sum += (x*y)
    print(sum)
