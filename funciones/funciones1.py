import random
sumar=0
def llenado(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista



def sumar(lista):
    sumar=0
    for i in  lista :
        sumar+=i
    return sumar 

def promedio(lista):
    promedio=sumar(lista)/len(lista)
    return promedio
    
def mayor(lista):
    mayor=0
    for k in lista:
        if k >mayor:
            mayor=k
    return mayor

def menor(lista):
    menor=0
    for e in lista :
        if e <menor:
            menor=e
    return menor

def ordenmayor(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista

def ordenmenor(lista):
    aux=0
    for e in range(len(lista)):
        for f in range(e+1,len(lista)):
            if lista[e]>lista[f]:
                aux=lista[e]
                lista[e]=lista[f]
                lista[f]=aux
    return lista
            
lista1=llenado(5,10)
print (lista1)
print(sumar(lista1))
print(promedio(lista1))
print(mayor(lista1))
print(menor(lista1))
print(ordenmayor(lista1))
print(ordenmenor(lista1))