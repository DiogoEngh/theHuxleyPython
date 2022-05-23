n = int(input())
def muda(x):
  res = ""
  for y in x:
    if y == "a" or y == "A":
      res += "4"
    elif y == "e" or y == "E":
      res += "3"
    elif y == "i" or y == "I":
      res += "1"
    elif y == "o" or y == "O":
      res += "0"
    else:
      res += y.upper()
  return res
for x in range(n):
  resu = ""
  frase = input().split()
  for k in frase:
    if k == frase[-1]:
        resu += muda(k)
    else:
        resu += muda(k) + " "
  print(str(x+1)+":"+resu)
