numero = int(input())
def par(n):
    if n%2 == 0:
        return True
    else:
        return False
      
digitos = []

def lista(n):
    if n>=0:
        digitos.append(n)
        return lista(n-1)
      
lista(numero)

for x in digitos:
  if par(x) == True:
    print(x)
