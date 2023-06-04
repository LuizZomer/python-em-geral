# def fatorial(n):
#     if n <=1:
#         return 1
    
#     return n * fatorial(n-1)



# print(fatorial(fat))

fat = int(input('Escolha um numero: '))
total = 1

for c in range(fat,1,-1):
    total *= c 

print(total)