def fatorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fatorial(n-1)
      
def multiplo3(n):
    if n%3 == 0:
        return True
    else:
        return False

soma = 0

for x in range(5):
    numero = int(input())
    if multiplo3(numero) == True:
        soma += fatorial(numero)
print(soma)
