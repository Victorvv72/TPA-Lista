n = 0
contador = 1
Maior = 0
while contador <= 10:
    n = int(input('Digite 10 valores: '))
    if Maior < n:
        Maior = n
    contador +=1
    
print (Maior)