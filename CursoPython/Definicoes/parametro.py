def soma(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} | {x+y+z}')
    else:
        print(f'{x=} {y=} | {x+y}')

soma(3,4,5)

