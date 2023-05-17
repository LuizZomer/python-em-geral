x = 1

def escopo():
    global x 
    x = 10

    def denovo():
        x = 2
        y = 4
        print(x,y)
    denovo()
    print(x)

escopo()
print(x)