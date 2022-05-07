def ordena(matriz):
  valores = []
  for numero in matriz:
    valores.append(float(numero[1].replace(",", ".")))
  maiorIndice = valores.index(max(valores))
  menorIndice = valores.index(min(valores))
  print("Menor:",str(min(valores)),"("+data(str(matriz[menorIndice][0]))+")")
  print("Maior:",str(max(valores)),"("+data(str(matriz[maiorIndice][0]))+")")
  print("Media:",str("%.2f"%(sum(valores)/len(valores))))

def data(valor):
  return valor.split("-")[1] + "-" + valor.split("-")[0]

listaIPCA = []

while True:
  ipca = input().split()
  if ipca ==["*"]:
    break
  else:
    listaIPCA.append(ipca)

ordena(listaIPCA)
