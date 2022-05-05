## usei como base para resolução a recursão em cauda

def verificaPar(digito):
  if int(digito)%2 == 0:
    return True
  else:
    return False
    
def contadorPar(numero):
  if numero == '':
    return 0
  else:
    x = numero[0]
    xs = numero[1:len(numero)]
    if verificaPar(x) == True:
      return 1 + contadorPar(xs)
    else:
      return contadorPar(xs)
      
numero = input()

print(contadorPar(numero))
