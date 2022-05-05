def repetidor(a,b):
    if a > 0:
        return repetidor(a-1, b) + b
    elif a == 0:
        return 0
    elif a < 0:
        return repetidor(a+1, b) - b
      
n1 = int(input())
n2 = int(input())

print(repetidor(n1,n2))
