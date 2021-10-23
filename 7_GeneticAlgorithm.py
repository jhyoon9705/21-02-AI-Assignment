# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 22:46:25 2021

@author: jhyoon
"""

import random

POPULATION_SIZE=4
MUTATION_RATE=0.1
SIZE=5

# 염색체를 class로 정의
class Chromosome:
    def __init__(self, g=[]):
        self.genes=g.copy()
        self.fitness=0
        if self.genes.__len__()==0:
            i=0
            while i<SIZE:
                if random.random()>=0.5: self.genes.append(1)
                else: self.genes.append(0)
                i+=1
            
    def cal_fitness(self):
        self.fitness=0;
        value=0
        for i in range(SIZE):
            value+=self.genes[i]*pow(2,SIZE-1-i)
        self.fitness=value
        return self.fitness
    
    def __str__(self):
        return self.genes.__str__()
    
# 염색체와 적합도 출력
def print_p(pop):
    i=0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.cal_fitness())
        i+=1
    print("")
    
# 선택 연산
def select(pop):
    max_value=sum([c.cal_fitness() for c in population])
    pick=random.uniform(0, max_value)
    current=0
    
    # 룰렛휠에서 어떤 조각에 속하는지 알아내는 루프
    for c in pop:
        current+=c.cal_fitness()
        if current>pick:
            return c
        
# 교차 연산
def crossover(pop):
    father=select(pop)
    mother=select(pop)
    index=random.randint(1, SIZE-2)
    child1=father.genes[:index]+mother.genes[index:]
    child2=mother.genes[:index]+father.genes[index:]
    return (child1, child2)

# 돌연변이 연산
def mutate(c):
    for i in range(SIZE):
        if random.random()<MUTATION_RATE:
            if random.random()<0.5:
                c.genes[i]=1
            else:
                c.genes[i]=0
                
population=[]
i=0

# 초기 염색체를 생성하여 객체 집단에 추가
while i<POPULATION_SIZE:
    population.append(Chromosome())
    i+=1
    
count=0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호= ", count)
print_p(population)
count=1

while population[0].cal_fitness()<31:
    new_pop=[]
    
    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2=crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))
        
    # 자식 세대가 부모 세대를 대체, 깊은 복사 수행
    population=new_pop.copy()
    
    # 돌연변이 연산
    for c in population: mutate(c)
    
    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호= ", count)
    print_p(population)
    count+=1
    
    if count>100: break;
        