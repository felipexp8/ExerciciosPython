#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:24:48 2019

@author: felipe

Exercícios 3 

em: https://github.com/advinstai/python/blob/master/Exercicios/lists-for-files-tuples-set-dict.md

usei o spyder para separar as células, igual no matlab com %%
    
    
"""

# %% A
x = [0, 1, [2]]
x[2][0] = 3
print x
x[2].append(4)
print x
x[2] = 2
print x

#a lista na terceira posição foi substituida interamente por um inteiro
# quando em faço x[2] e este elemento é uma lista ou conjunto com outros elementos
# este item vira ponteiro, sendo assim podemos alterar valores internamente 
# sem mudar a estrutura da lista

# %% B


print sum([1, 2, 3])
    
# %% C

sum(["hello", "world"])
     
sum(["aa", "bb", "cc"])
  
#String não faz somas, faz concatenação, no p2.7 dá erro

# %% D

def product(listagem):
    aux = 1
    for x in listagem:
        aux*=x #não é ponteiro
    return aux  

print product(range(1,10)) 

# %% E

def fatorial(valor):
    return product(range(1,valor+1))

print fatorial(3)

# %% F

def reverso(listagem):
    aux = list()
    for i in range(len(listagem)-1,-1,-1):
        aux.append(listagem[i])
    return aux

reverso([2,3,4,5])
        
#sem usar o slicing e o reverse, também pode ser implementado por fila FIFO

# %% G

min(["string", "outraString"])
max(["string", "outraString"])

# ele fez, porém usa como critério o primeiro char de cada string, os demais
# ele ignora

# %% H

# obs: No python tem MAP e REDUCE

def cumsum(listagem):
    out = list()
    aux = 0
    for x in listagem:
        aux+=x
        out.append(aux)
    return out

#Serie de Fibonacci
cumsum([1,2] + range(1,10))

# %% I

def produtorio(listagem):
    out = list()
    aux = 1
    for x in listagem:
        aux*=x #não é ponteiro
        out.append(aux)
    return out

produtorio([1,2,3,4])  

# %% J

def unico(listagem):
    return set(listagem)

#posso fazer: unique=set
unico([ 1,1,1,1,2,3,3,5,6])

# %% H

def dup(listagem):
    
    out = list()
    
    iterador = 0
    
    for elemento in listagem:
        if elemento in listagem[0:iterador]:
            out.append(elemento)
        iterador+=1
    return set(out) 
            

print dup([1,2,2,3,3,4,9,4,5,5,5])
    
# %% I

#sei que tem pronto, mat2vec faz isso

def group(listagem,nGrupos):
    aux = list()
    posicao=0
    for x in range(0, len(listagem) // nGrupos + len(listagem) % nGrupos):
        aux.append(listagem[posicao:posicao+nGrupos])
        
        posicao=posicao+nGrupos

    return aux

group([1,2,3,4,5,6,7,8,9,10,11],5)

# %% J

def ordenar(strList):
    strList.sort(key=lambda x: len(x))
    return list(strList) #força copiar str list

# %% K
    
def unicoK(listagem = None, key = None):
    if key == None:
        return set(listagem)
    else:
        return set(map(key,listagem))

unicoK(["aA", "aa", "b"], lambda s: s.lower())
    

# %% L

# já fiz

unique = set

# %%  M

def sortex(listagem):
    
    listagem.sort(key=lambda x: x.split(".")[1])
    
    return list(listagem)

sortex(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

# %% N


arquivo = open("she.txt", "r")

porcao = arquivo.readlines()

reverso = porcao[::-1]

arquivo.close()

arquivo = open("she.txt", "w")

arquivo.writelines(reverso)

arquivo.close()

# %% O

arquivo = open("she.txt", "r")

porcao = arquivo.readlines()

reverso = porcao[::-1]

for linha in reverso:
    print linha

# %% P
    
import os

def headfile(arquivo):
    os.system("head " + arquivo)

def tailfile(arquivo):
    os.system("tail " + arquivo)

# %% Q
    
#usar argc argv para o console:
arquivo = open("she.txt", "r")

porcao = arquivo.readlines()



def procuraPalavra(listastr, palavra):
    res = list()
    for linha in listastr:
        aux = linha.split(" ")
        
        if palavra in aux:
            res.append(linha)
    return res

        
    
    
