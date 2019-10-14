#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:56:00 2019

@author: felipe

Gera anagramas via codigo genetico e padrões de artifícios (gambiarras)
"""

import random as rnd


#padrão de gambiarra: Uso da Caballa
rnd.seed(666)

#padrao de gambiarra: o que o homem pode fazer, ele faz

genes = "abcdefghijklmnopqrstuvwxyz"

genes = list(genes) #cast to Char*

# Padrão de gambiarra: Que a sorte nos separe

def criterio(string1,string2):
    """
    faz o criteŕio de parada, reconhece quando uma string é anagrama de outra
    faz uma tecnica parecida como o checksum, mas a quinta potência, a chance de ser igual para
    string diferentes é muito baixa (p ~ -100dB)
    """
    
    if len(string1)!=len(string2): 
        return False
    
    a = sum( ord(x) ** 5 for x in string1)
    b = sum( ord(x) ** 5 for x in string2)
    
    return a==b

# Padrão de gambiarra: Fenix, apenas 1 sobrevive, então vale população de 1
    
def evolua(final, geracao=1000000):
    n = len(final)
    word = ['a'] * n #apenas uma amostram com todos os genes A
    
    for el in range(geracao):
        
        for x in range(n):
            word[x]=rnd.choice(genes)  #Faz a mutação
        
        if criterio(word,final): return word
       
        
# para gerar um anagrama válido chame o evolua("palavra")





