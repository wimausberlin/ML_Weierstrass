# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:26:45 2021

@author: wimpo
"""
import random as rd
from math import *
from operator import itemgetter
# %% Generate the population
def generate_individual():
    a=0
    while a==0: #0 excluded
        a,b,c=rd.random(),rd.randint(1,20),rd.randint(1,20)
    return [a,b,c]

def generate_population(n):
    pop=[]
    for i in range(n):
        pop.append(generate_individual())
    return pop
# %%

def euclidean_distance(individual):
    resultW=resultWeierstrass(individual)
    score=0
    for element in resultW:
        score+=pow(element[1]-element[2],2)
    return sqrt(score)

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
    for k in range(int(individual[2])):
        result+=pow(individual[0],k)*cos(individual[1]*pi*i)
    return result

def fitness(individual):
    return euclidean_distance(individual)

def select(population):
    indi=population[0]
    fitness_score=fitness(population[0])
    for individual in population:
        if fitness_score>fitness(individual):
            fitness_score=fitness(individual)
            indi=individual
    return indi

def crossover(population):
    popuCrossover=[]
    gene=select(population)
    for i in range(1,len(population)):
        #newIndi=gene if rd.choice([True,False]) else population[i]
        crossoverA=gene[0] if rd.choice([True,False]) else population[i][0]
        crossoverB=gene[1] if rd.choice([True,False]) else population[i][1]
        crossoverC=gene[2] if rd.choice([True,False]) else population[i][2]
        newIndi=[crossoverA,crossoverB,crossoverC]
        popuCrossover.append(newIndi)
    return popuCrossover

def mutation(population):
    for individual in population:
        index=rd.randint(0,2)
        if(index==0):
            individual[0]=rd.random()
        elif(index==1):
            individual[1]=rd.randint(1,20)
        else:
            individual[2]=rd.randint(1,20)

def fillpop(population):
    populationNew=[]
    populationNew.append(select(population))
    populationNew.extend(crossover(population))
    mutation(populationNew)
    return populationNew
"""
def fitness_score(population):
    for individual in population:
        score=euclidean_distance(individual)
        individual.append(score)
        #print(score)

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

def euclidean_distance(individual):
    resultW=resultWeierstrass(individual)
    score=0
    for element in resultW:
        score+=pow(element[1]-element[2],2)
    return sqrt(score)
def weierstrassFunct(individual,i):
    result=0
    for k in range(int(individual[2])):
        result+=pow(individual[0],k)*cos(individual[1]*pi*i)
    return result

def sort(population):
    population.sort(key = lambda x: x[3])

def select(population):
    popu=population.copy()
    sort(popu)
    mid=len(popu)//2
    if len(popu)%2==1:
        mid+=1
    # for element in population:
    #     element.pop(3)
    return popu[0:mid]

def crossover(population):
    pop=[]
    for i in range(0,len(population)-1,2):
        a=(population[i][0]+population[i+1][0])/2
        b=(population[i][1]+population[i+1][1])//2
        c=(population[i][2]+population[i+1][2])//2
        pop.append([a,b,c])
    return pop

def mutation(population):
    for individual in population:
        mutationIndi(individual)

def mutationIndi(individual):
    if(rd.choice([True, False])):
        diff=rd.uniform(-0.3, 0.3)
        if(individual[0]+diff <1 and individual[0]+diff >0):
            individual[0]+=diff
    if(rd.choice([True, False])):
        diff=rd.randint(-2, 2)
        if(individual[1]+diff <=20 and individual[1]+diff>=1):
            individual[1]+=diff
    #if(rd.choice([True, False])):
    diff=rd.randint(-5, 5)
    if(individual[2]+diff <=20 and individual[2]+diff>=1):
        individual[2]+=diff
      
def fillpop(population):
    fitness_score(population)
    #print(population[0][3])
    popN=select(population)+crossover(population)
    mutation(popN)
    fitness_score(popN)
    return popN

def showAll(popN):
    for i in range(len(popN)):
        show(popN,i)

def show(popN,index):
    print("a=",popN[index][0],"b=",popN[index][1],"c=",popN[index][2])    
 
def sumScore(popN):
    scoreS=0
    for i in range(len(popN)):
        scoreS+=popN[i][3]
    return scoreS/len(popN)
"""
def init():
    population=generate_population(10)
    i=0
    while(fitness(population[0])>1):
        population=fillpop(population)
        i+=1
        #print(fitness(population[0]))    
        print(population[0])
# %% main
if __name__=="__main__" :
    init()