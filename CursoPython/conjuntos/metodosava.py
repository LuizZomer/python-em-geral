s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 # O sinal '|' Significa uniao dos set

print(s3)

s3 = s1 & s2 #O '&' significa itens presentes em ambos

print(s3)

s3 = s1 - s2 #O '-' siginifica diferença 
s4 = s2 - s1 # Quem vem primeiro importa

print(s3)
print(s4)

s3 = s1 ^ s1 #O '^' vai mostrar os itens que não estão presentes em ambos