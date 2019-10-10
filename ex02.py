# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário
Para exercicios: https://github.com/advinstai/python/blob/master/Exercicios/Lista2.md

"""

#ex 1


#A 

1+2

# Aparece apenas no juypter e no modo interativo
# no modo script sem os complementos eh preciso usar o print

#B

x=4
y=x+1
x=2

print(x,y)

#  ele fez as atribuicoes, mostrou o x atual e o y incrementado
# da primeira versao do x

#C


a, b = 2, 3
# c, b = a, c + 1

print( a, b, 0)

# Erro: c nao declarado

#D

numcalls = 0

def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x ** 2

print (square(5))
print (square(2*5))

# ele altera o numcalls, pois é global, nas na funcao e preciso indicar que nao
# é uma variavel automatica e sim uma externa


#E

x = 1

def f():
    x = 2
    return x
print (x)
print (f())
print (x)

# x dentro de f é uma variável local (automática)

#F

x = 2   

def f(a):
    x = a * a
    return x

y = f(3)

print (x, y)

# x=2 fora de f(a) e x em f(a) é uma variavel automática

#G Comparando duas string sem case sensitive:

print("oi".lower()=="OI".lower())

#H Digitos de inteiros:

ver = "%i" % 5

print(len(ver))

ver = "%i" % 54545

print(len(ver))


#I

print (2 < 3 and 3 > 1)
print (2 < 3 or 3 > 1)
print (2 < 3 or not 3 > 1)
print (2 < 3 and not 3 > 1)

#tabela verdade {True, True, True False}

#J

x = 4
y = 5
p = x < y or x < z
print (p)

#ele verifica x e y  e faz a operacao OR
#o python converte automaticamente Bool para STR quando imprime

#K

#True, False = False, True
#print True, False
#print 2 < 3

#Não pode atribuit a constantes
#True é sempre 1 e False é sempre 0

#L


x = 2
if x == 2:
    print (x)
else:
    print (y)

#y nao declarado mas não dá erro, pois a condição
# que chama ele nunca é atendido (válido apenas para linguagens interpletadas)

# M
    
 '''
x = 2
if x == 2:
    print (x)
else:
    x +
    
'''

#invalid syntax: mesmo sendo uma condição que nao acontece, 
#é preciso finalizar a expressao


#ex2
    
#A

enunciado = "Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles"

print(enunciado)

a = input("coloque um valor para A:")
b = input("coloque um valor para B:")    

print( "o maior valor entre eles é: " + str ( max([a,b]) ) )

#B

enunciado = " Para doar sangue é necessário: \n \
\
    Ter entre 16 e 69 anos \n \
    Pesar mais de 50 kg \n \
    Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)."

print(enunciado)

idade = input("sua idade")
peso = input("seu peso")

descanso = input("Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas). [y/n])" )
    
bdescanso = True if descanso == 'y' else False

if (idade in range(16,69)) and peso > 50 and bdescanso:
    print("pode doar sangue")
else:
    print("Não pode")
    
#C

a,b,c = [1]*3

delta = b**2 - 4*a*c

if delta = 0:
    print("uma raiz")
if delta > 0:
    print("duas raizes positivas")
if delta < 0:
    print("raizes complexas")


#D

import random as rnd

#usar rnd no lugar do usuário digitar

num1 = rnd.randint(0,100)
num2 = rnd.randint(0,100)

res = num1 + num2

if res >20:
    res+= 8
else:
    res-= 5
    
print (res)

#E

num1 = rnd.randint(-100,100)

if num1 >= 0:
    print(pow(num1,1/2))
else:
    print(num1 ** 2)
    
#F

mes = int(input("digite um mês (em números): \n"))

if not mes in range(1,12):
    print("este mês informado não existe")
