# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 2021

@author: Wim Poignon TD G
"""
import random as rd
from math import *
from operator import itemgetter
import time
# %% Generate the population
def generate_individual():
    a,b,c=rd.randint(1,99)/100,rd.randint(1,20),rd.randint(1,20)
    return [a,b,c]

def generate_population(n):
    pop=[]
    for i in range(n):
        pop.append(generate_individual())
    return pop
# %% Operations
def mutation(individual):
    individualNew=individual.copy()
    proba=rd.random()
    if(proba<2/3):
        individualNew[0]=rd.randint(1,99)/100
    else:
        index=1 if(rd.randint(0,1)) else 2
        individualNew[index]=rd.randint(1, 20)
    return individualNew
def crossover(indi1,indi2):
    a1,b1,c1=indi1[0],indi1[1],indi1[2]
    a2,b2,c2=indi2[0],indi2[1],indi2[2]
    indi1New=[a2,b1,c2]
    indi2New=[a1,b2,c1]
    return indi1New,indi2New
def select(population,percentBest,percentWorst):
    tabSelect=[]
    length=len(population)
    indexBest=int(length*percentBest/100)
    indexWorst=int(length*percentWorst/100)
    for i in range(0,indexBest):
        tabSelect.append(population[i])
    for i in range(0, indexWorst):
        tabSelect.append(population[length-1-i])
    return tabSelect
def evaluate(population):
    tabSorted=sorted(population, key=lambda indi:fitness(indi))
    return tabSorted

def fillpop(population):
    percentBest,percentWorst,percentMutation=30,10,30
    tabSelect=select(population,percentBest,percentWorst)
    cross=[]
    for i in range(0,len(tabSelect),2):
        if (i+1<len(population)):
            cross.append(crossover(population[i],population[i+1])[0])
            cross.append(crossover(population[i],population[i+1])[1])
    lengthRest=len(population)-len(tabSelect)-len(cross)
    newalea=generate_population(lengthRest)
    newPop=tabSelect[:]+cross[:]+newalea[:]
    times=int(len(newPop)*percentMutation/100)
    for i in range(0,times):
        indexRand=rd.randint(0,len(newPop)-1)
        newPop[indexRand]=mutation(newPop[indexRand])
    return newPop

# %% Functions
def fitness(individual):
    resultW=resultWeierstrass(individual)
    score=0
    for element in resultW:
        score+=abs(element[1]-element[2])
    return score/len(resultW)

def resultWeierstrass(individual):
    tab=[]
    with open("temperature_sample.csv",'r') as file:
        tabLines=file.read().splitlines()
        tabLines.pop(0) #delete first line with i and t
        for element in tabLines:
            i=float(element.split(";")[0])
            t=float(element.split(";")[1])
            tgenerate=weierstrassFunct(individual,i)
            IRG=[i,t,tgenerate]
            tab.append(IRG)
    return tab

def weierstrassFunct(individual,i):
    result=0
    for k in range(individual[2]):
        result+=individual[0]**k*cos(pi*i*individual[1]**k)
    return result

# %% Algo genetic
def init():
    start = time.time()
    population=generate_population(50)
    nbriteration=0
    solutionFound=False
    count=0
    individualBefore=population[0]
    while not solutionFound:
        evaluation=evaluate(population)
        nbriteration+=1
        if(evaluation[0]==individualBefore):
            count+=1
        else:
            count=0
            individualBefore=evaluation[0]        
        if(fitness(evaluation[0])<0.04):# or count>20):
            solutionFound=True
        else:
            population=fillpop(evaluation)
    end = time.time()
    temps=end-start
    print("Combinaison:",population[0])
    print("Nombre d'itérations:",nbriteration)
    print("Temps d'exécution:",round(temps,2),"secondes")

# %% main
if __name__=="__main__" :
    init()