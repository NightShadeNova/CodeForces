x = int(input())
s = 0
for _ in range(x):
    i = input()
    if i == 'X++' or i =='++X' or i == '+X+':
        s += 1
    else:
        s -= 1
print (s)
        
