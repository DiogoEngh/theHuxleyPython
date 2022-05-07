listaGeral = []
def ordenaNomes(lista):
  head = min(lista)
  menores = lista[0:lista.index(head)]
  maiores = lista[lista.index(head)+1:len(lista)]
  tail = menores + maiores
  if tail == []:
    return [head]
  else:
    return [head] + ordenaNomes(tail)
while True:
  nome = input()
  if nome == 'FIM':
    break
  elif nome not in listaGeral:
    listaGeral.append(nome)
while True:
  nome = input()
  if nome == 'FIM':
    break
  elif nome not in listaGeral:
    listaGeral.append(nome)
novaLista = ordenaNomes(listaGeral)
for nomes in novaLista:
  print(nomes)
