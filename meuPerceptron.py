#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:36:34 2019

@author: felipe

rede neural vanilla

teste simples de classificação
"""

import numpy as np

import pylab as plot

pesos = np.array([0.5 , -0.5])

Sa = 1 #taxa de amostragem

x1 = np.arange(1,10,Sa)

x2 = np.arange(1,10,Sa)

def neuro(valores, pesos, offset=1):
    if type(valores)==type(pesos)==np.ndarray: #TODO: validar antes de chamar esta funcao
        return sum(valores*pesos) > offset  #funcao heaviside d[x-offset]
    # sem o numpy faze:r sum ( x*y for x,y in zip(valores,pesos) )
    else:
        return "NaN"


saida = list()

for i in x1:
    for j in x2:
        xn = np.array([i,j])
        saida.append( neuro( xn, pesos,1) )
    
print sum(saida)

 
pointsX = list()
pointsY = list()

#converte uma funcao a fim em um espaco geografico
for x in x1:
    pointsX += [x for y in x2]
    
for x in x2:
    pointsY += [x for x in x1]

plot.scatter(pointsX,pointsY)

pointsYres = np.array(pointsY)*saida

plot.grid(); plot.scatter(pointsX,pointsYres)





