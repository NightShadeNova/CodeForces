n = list(input())
a = 0
for i in range(len(n)-6):
  for j in range(1, 7):
    if n[i] == n[i+j]:
      a = 1
    else:
      a = 0
      break  
  if a == 1:
    break
if a == 1:
  print("YES")
else:
  print("NO")
