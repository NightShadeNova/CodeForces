n = int(input())
stones = input()
x = 0
for i in range(n-1):
    if stones[i] == stones[i+1]:
        x += 1
print(x)
