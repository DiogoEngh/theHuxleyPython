def fib(numero):
  if numero == 0:
    return 1
  if numero == 1:
    return 1
  else:
    return numero * fib(numero-1)
  
while True:
  numero = int(input())
  if numero == -1:
    break
  else:
    print(fib(numero))
