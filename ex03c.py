#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:24:48 2019

@author: felipe

Exercícios 3 

em: https://github.com/advinstai/python/blob/master/Exercicios/lists-for-files-tuples-set-dict.md
    
    
"""

# %% A
x = [0, 1, [2]]
x[2][0] = 3
print (x)
x[2].append(4)
print (x)
x[2] = 2
print (x)

#a lista na terceira posição foi substituida interamente por um inteiro
# quando em faço x[2] e este elemento é uma lista ou conjunto com outros elementos
# este item vira ponteiro, sendo assim podemos alterar valores internamente 
# sem mudar a estrutura da lista

# %% B


print ( sum([1, 2, 3]) )
    
# %% C

'''  
sum(["hello", "world"])
     
sum(["aa", "bb", "cc"])
'''
#String não faz somas, faz concatenação, no p2.7 dá erro

# %% D

def product(listagem):
    aux = 1
    for x in listagem:
        aux*=x #não é ponteiro
    return aux  

print (product(range(1,10)) )

# %% E

def fatorial(valor):
    return product(range(1,valor+1))

print ( fatorial(3) )

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
            

print ( dup([1,2,2,3,3,4,9,4,5,5,5]) )
    
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
    print ( linha )

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

# %% 22
    
def wrapfrase(tamanho, texto):
    aux = list()
    for elemento in texto:
        aux.append(elemento[0:tamanho])
    return aux

# %% 23
    
def wordwrap(tamanho, texto):
    aux = list()
    for linha in texto:
        nlinha = str()
        for x in range(len(linha)):
            nlinha+= linha[x]
            if x > tamanho:
                if linha[x] == ' ':
                    break
                else:
                    continue
        aux.append(nlinha)
        
    return aux
    
# %% 24
    
def centerText(texto):
    maximo =  max(list(map(len, texto))) #python 3.7 requer o list antes do map
    
    resultado = list()
    
    for linha in texto:
        ajuste = (maximo - len(linha)) // 2
        
        nova_linha = "".join(["_"]*ajuste) #cria uma string de tamanho fixo e preenchida
        
        nova_linha+= linha + nova_linha
        
        resultado.append(nova_linha)
    
    return resultado


        
# %% 25 

# Provide an implementation for zip function using list comprehensions.

def mdual(lista1, lista2):
    if len(lista1) != len(lista2): return
    
    iterador = 0
    aux = list()
    
    for x in lista1:
        aux.append  ( [x, lista2[iterador]] )    
        iterador+=1
    
    return aux

# %% 26
    
# Python provides a built-in function map that applies a function to each 
# element of a list. Provide an implementation for map using list comprehensions.

def mmap(lista, void):
    return [void(x) for x in lista ]

# %% 27
    
def mfilter(lista, void):
    return [x for x in lista if void(x) ]

# %% 28
    
def trivale(maximo): 
    """
    não otimizado
    """    
    possibilidades = []
     
    for x in range(1,maximo):
    
        #bloco de força bruta:
        for i in range(x):
            for j in range(x): 
                #exemplo: até 5 temos 3 e 4 cuja soma passa de 5
                if i+j == x:
                    possibilidades.append( (i,j,x) )
                #else: loop disperdiçado
            
    return possibilidades

# %% 29
    
def enumerar(listagem):
    return  list ( zip( range(len(listagem)) ,  listagem) )
        
        
# %% 30

def array(n,m):
    ma = [None]*m
    
    for x,y in enumerar(ma):
        ma[x] = [None]*n
    
    return ma

# %% 31
    
def parseCSV(textol):
    
    if type(textol)==list:
    
        listagem = list()
        
        for linha in textol:
            atual = linha.split(",")
            listagem.append(atual)
            
        return listagem

    else:
        try:
            
            textom = textol.split("\n")
            
            listagem = list()
            
            for linha in textom:
                listagem.append(linha.split(","))
            
            return listagem
        
        except:
            print("formato invalido")
            return None
        
# %% 32
    
def parse2CSV(textol,marca=",", comentario="#"):

    if type(textol)==list:
    
        listagem = list()
        
        for linha in textol:
            atual = linha.split(comentario)
            atual = atual[0].split(marca)
            listagem.append(atual)
            
        return listagem

    else:
        try:
            
            textom = textol.split("\n")
            
            listagem = list()
            
            for linha in textom:
                atual = linha.split(comentario)
                atual = atual[0].split(marca)
                listagem.append(atual)
            
            return listagem
        
        except:
            print("formato invalido")
            return None       
        
# %%
            
# problem 33: Write a function mutate to compute all words generated by a single 
# mutation on a given word. A mutation is defined as:
# - inserting a character, 
# - deleting a character, 
# - replacing a character, 
# - swapping 2 consecutive characters 
# in a string. For simplicity consider only letters from a to z.
            

def insC(palavra): #replacing
    
    mword = list(palavra)
    
    listagem = set()
    
    #gera de a até z
    words = [chr(x) for x in range(97,122) ] #ord("a") ~ord("z") 
    
    for x in range(len(mword)):
        for char in words:
        
            word = list(mword) # cast de string para char*
        
            word[x] = char
        
            listagem.add("".join(word))
    
    return listagem

def insMaisC(palavra): #inserting
    
    mword = list(palavra)
    
    listagem = set()
    
    #gera de a até z
    words = [chr(x) for x in range(97,122) ] #ord("a") ~ord("z") 
    
    for x in range(len(mword)):
        for char in words:
        
            word = list(mword) # cast de string para char*
        
            word = word[0:x] + [char] + word[x::] #colocar uma char no meio
        
            listagem.add("".join(word))
    
    return listagem
        
def delChar(palavra): 
    
    listagem = set()
    
    mword = list(palavra) # cast de String para char*
    
    for x in range ( len(palavra) ):
        
        word = list(mword) # clone
        
        del word[x]
        
        listagem.add("".join(word))
        
    return listagem

def swap(palavra):
    
    listagem = set()
    
    mword = list(palavra)
    
    for x in range( len(palavra ) -1 ) :
        
        word = list(mword) # clone
        
        a = word[x+1]
        b = word[x]
        
        word[x] = a
        word[x+1] = b 
        
        listagem.add("".join(word))
        
    return listagem


def mutate(palavrao):
    
    mutacao = list()
    
    mutacao = list(swap(palavrao))
    
    mutacao+= list(delChar(palavrao))
    
    mutacao+= list(insC(palavrao))
    
    mutacao+= list(insMaisC(palavrao))
    
    
    return mutacao
    
# %% 
    
# problem 34: Write a function nearly_equal to test whether two strings are nearly
# equal. Two strings a and b are nearly equal when a can be generated by a single mutation on b.
    
def verificaMutate(palavra1, palavra2):
    
    listagemCompara = mutate(palavra2)
    
    compara = palavra1 in listagemCompara
    
    return compara
    
    
    
        
        


        
    
        
        
# %% dicionarios 
            
#problem 36: Write a program to count frequency of characters in a given file. 
#Can you use character frequency to tell whether the given file is a Python program file,
#C program file or a text file?
 
path="she.txt" 
    
arquivo = open(path, "r") #negligenciei exceções pois esetou num Bloco

fconteudo = arquivo.readlines()

def histchar(texto):

    """
    Solução não otimizada
    """
    histo = dict()
    
    serie = "".join(fconteudo) #serializa tudo
    
    #aloca o histograma
    for char in serie: #no python a palavra reservada é chr
        histo[char] = 0;
    
    #conta o histograma
    for char in serie:  
        histo[char] +=1

    return histo

## Em C tem mais ";" e mais "{}" para cada função implementada
    
# %% 
    
#problem 37: Write a program to find anagrams in a given list of words. 
#Two words are called anagrams if one word can be formed by rearranging 
# letters of another. For example 'eat', 'ate' and 'tea' are anagrams.

import random as rand



def virador(mstring): # "ordo ab chaos"
    
    """
    AVISO: náo otimizado, muito ineficiente
    """
    
    pilha = [x for x in mstring]
    
    wcaos = ""
    
    iterador = len(mstring)
    
    
    atual = rand.choice(pilha)
    
    wcaos+= atual
    
    while(iterador>1): #TODO: fazer o POP da pilha ou DEL
        
        atual = rand.choice(pilha)
        
        if atual in wcaos:
              continue
        else:
            iterador-=1
            wcaos += atual
            continue
        
    return wcaos


def anagrama(mstring, brutalizador=100, tamanho=0):
    
    
    balde = set()
    
    for x in range(brutalizador):
        
        balde.add(virador(mstring))
        
    if tamanho>0:
        return list(balde)[0:tamanho]
    else:
        return list(balde)

def procuraanagrama(listPalavras):
    
    grupos = dict()
    
    for i in range(len(listPalavras)):
        
        palavras = anagrama(listPalavras[i])
      
        for j in range(len(listPalavras)):
            
            if i==j: continue
            
            if (listPalavras[j] in palavras):
                
                try:
                    grupos[i].append( listPalavras[j])
                except:
                    grupos[i] = list()
                    grupos[i].append(listPalavras[i])
                    grupos[i].append(listPalavras[j])
                    
    #até aqui separou em dict, mas com elementos repetidos e bagunçados
    
    aux = list()
    
    for elemento in grupos.items():
        
        elemento[1].sort() # para usar o SET precisa juntar todos os itens num só
        
        aux.append(";".join(elemento[1]))
        
    res = set(aux)  #resultado (separado por ;)
    
    aux2 = list()
    
    for elres in res:
        aux2.append(elres.split(";"))
    
    return aux2
            
            
            
            
            
            
        


# %%

# Write a function valuesort to sort values of a dictionary based on the key.

#suponde chave string e valor inteiro

def orgChave(diclist):
    
    converte = [x for x in  diclist.items() ] #cast dictItens para List com tuplas
    
    converte.sort(key=lambda x: x[1]) # o segundo elemento da tupla é o critério
    
    return converte
    

# %%
    
def inverDict(mdict):
    
    converte = [x for x in  mdict.items() ] #cast dictItens para List com tuplas
    
    novo = dict()
    
    for k,v in converte:
        novo[v] = k
        
    return novo
        
        
 # %%   
    
    

        
    
    
