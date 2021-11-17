
n = int(input())
x = 0
while(n>0):
    y = 0
    z = input()
    for i in z:
        if i == '1':
            y += 1
    
    if y > 1:
        x += 1
    n -= 1
print(x)
   
