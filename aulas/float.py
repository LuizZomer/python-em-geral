from decimal import Decimal

x = Decimal('0.1')
y = Decimal('0.7')
z = x + y

print(z)
print(f'{z:.2f}')
print(round(z,3))