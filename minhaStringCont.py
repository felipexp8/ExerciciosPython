#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:56:05 2019

@author: felipe

Tarefa python OO

"""

'''

Modele uma classe que realiza as seguintes operações em um arquivo texto

    - Represente um texto como uma lista de Strings
    - Retorne individualmente cada palavra do texto
    - Conte a quantidade de ocorrências de cada palavra do texto
    - Retorne as 10 palavras mais frequentes
    - Retorne a média e desvio padrão da quantidade de ocorrências
    - Cadastre StopWords (A classe deve possuir um atributo com uma lista de StopWords)
    - Retorne um novo arquivo eliminando todas as StopWords do texto
    - Inclua um método que retorne a distância entre duas palavras

'''

import math

#Gambi Patter: o computador faz, não precisa organizar o texto
stopwords = "de,a,o,que,e,do,da,em,um,para,é,com,não,uma,os,no,se,na,por,mais,\
as,dos,como,mas,foi,ao,ele,das,tem,à,seu,sua,ou,ser,quando,muito,há,nos,já,está\
,eu,também,só,pelo,pela,até,isso,ela,entre,era,depois,sem,mesmo,aos,ter,seus,\
quem,nas,me,esse,eles,estão,você,tinha,foram,essa,num,nem,suas,meu,às,minha,têm,\
numa,pelos,elas,havia,seja,qual,será,nós,tenho,lhe,deles,essas,esses,pelas,este,\
fosse,dele,tu,te,vocês,vos,lhes,meus,minhas,teu,tua,teus,tuas,nosso,nossa,nossos,\
nossas,dela,delas,esta,estes,estas,aquele,aquela,aqueles,aquelas,isto,aquilo,estou,\
está,estamos,estão,estive,esteve,estivemos,estiveram,estava,estávamos,estavam,\
estivera,estivéramos,esteja,estejamos,estejam,estivesse,estivéssemos,estivessem,\
estiver,estivermos,estiverem,hei,há,havemos,hão,houve,houvemos,houveram,houvera,\
houvéramos,haja,hajamos,hajam,houvesse,houvéssemos,houvessem,houver,houvermos,\
houverem,houverei,houverá,houveremos,houverão,houveria,houveríamos,houveriam,sou,\
somos,são,era,éramos,eram,fui,foi,fomos,foram,fora,fôramos,seja,sejamos,sejam,\
fosse,fôssemos,fossem,for,formos,forem,serei,será,seremos,serão,seria,seríamos,\
seriam,tenho,tem,temos,tém,tinha,tínhamos,tinham,tive,teve,tivemos,tiveram,tivera,\
tivéramos,tenha,tenhamos,tenham,tivesse,tivéssemos,tivessem,tiver,tivermos,tiverem,\
terei,terá,teremos,terão,teria,teríamos,teriam".split(",")

class MyString:
    
    def __init__(self, texto=None, semVirgula = False):
        
        if(type(texto)==list):
            self.texto = "".join(texto).lower()
        else:
           self.texto = texto.lower()
        
        try:
            
            self.palavras = self.texto.replace('\n', "\x20")
            
            if semVirgula: self.texto.replace(",","")
            
            self.palavras = self.texto.split("\x20")
            
        except BaseException as e:
            
            self.linhas = ""
            
            print "falha no formato das palavras", e.args
        
        self.hist = dict()
        
        self.__stopwords = list()
        
    def countWord(self):
        
        palavras = self.palavras
        
        if len(palavras)==0: raise NameError("não há frases aqui")
            
        self.hist = dict()
        
        for x in palavras: self.hist[x] = 0 #aloca o dicionario para virar histograma 
        
        for n in palavras: self.hist[n] += 1 #faz a contagem
    
    def count10(selft):
        
        listagem = [x for x in self.hist.items()] #cast Dict para List em Tuple
        
        listagem.sort(key=lambda x: x[1],reverse=1) #ordena lista com base no segundo elemento da tupla
        
        if len(listagem>9): return listagem[0:10]
        else: return listagem
        
    def mean(self):
        
        return sum( x for x in self.hist.values()  ) / len(self.hist)
        
    def desvpa(self):
        
        u = self.mean()
        
        sigma = sum( (xi-u)**2 for xi in self.hist.values()  ) / len(self.hist)
        
        return math.sqrt(sigma)
     
    @staticmethod
    def hamming(p1, p2): # distancia de hamming (lá das telecomunicações)
    
        if len(p1)!=len(p1): return -1 #palavras devem ser iguais
    
        palavra1 = map(ord,p1) #cast String para uchar*
        
        palavra2 = map(ord,p2) 
        
        xor = map(lambda x: x[0]^x[1], zip(palavra1,palavra2) )
        
        return sum (bin(x).count("1") for x in xor)
    
    def addStopWord(self,word):
        self.__stopwords.append(word)
    
    def removeContentStopWord(self):
        
        textoOut=str(self.texto)
        
        for palavra in self.__stopwords:
            textoOut=textoOut.replace(palavra,"")
        
        
    def removeStopWord(self):
        for i,elemento in enumerate(self.palavras):
            if (elemento in stopwords): del self.palavras[i]
    
    
    def limpeza(self):
         self.palavras = [x for x in self.palavras if x!='']
