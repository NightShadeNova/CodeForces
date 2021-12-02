str1 = input()
str1 = str1.lower()
str2 = input()
str2 = str2.lower()
x = 0
for i in range(len(str1)):
    if ord(str1[i]) == ord(str2[i]):
        pass
    elif ord(str1[i]) >= ord(str2[i]):
        x = 1
        break
    else:
        x =-1
        break
print (x)
