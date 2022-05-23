cartao = input()
valorCompra = float(input())
limite = float(input())
tg = 0.01*valorCompra
tp = 0.025*valorCompra
ti = 0.05*valorCompra
def compra(c):
  if c.lower() == 'gold':
    if tg >= limite:
      print('%.2f'%limite)
    else:
      print('%.2f'%tg)
  elif c.lower() == 'platinum':
    if tp >= limite:
      print('%.2f'%limite)
    else:
      print('%.2f'%tp)
  elif c.lower() == 'infinity':
    print('%.2f'%ti)
compra(cartao)
