n = int(input())
for _ in range(n):
    ith = input()
    if len(ith) > 10:
        x = ith[0] + str(len(ith)-2) + ith[-1]
        print(x)
    else: 
        print(ith)
