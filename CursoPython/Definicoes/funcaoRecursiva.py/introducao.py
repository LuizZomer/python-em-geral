import sys
sys.setrecursionlimit(2000)

def recursiva(inicio=0,fim=10):
    print(inicio,fim)
    if inicio >= fim:
        return fim
    inicio +=1
    return recursiva(inicio,fim)
     

print(recursiva(0,2000))