import random
import math
import numpy as np
import copy

class Producer:
   
    def __init__(self, id, goal, genre, strategy):
        self.id = id
        self.curr_funds = 0
        self.total_ad_spending = 0
        self.campaign_goal = goal
        self.genre = genre
        self.contributors = {}
        self.strategy = strategy
        self.averageMarketPrefrence = [.55]
        self.goalComplete = -1

    def advertise(self, graph, marketAnalysis,step):
        self.averageMarketPrefrence.append(math.tanh(np.random.normal(marketAnalysis,3)))
        
        if self.campaign_goal <= self.curr_funds:
            spendAmount = 0
            if self.goalComplete == -1:
                self.goalComplete = step
        else:
            spendAmount = self.advertiseBudget * self.getMarketAverage()
         
        if spendAmount > 1:
            self.total_ad_spending += spendAmount
            self.advertiseBudget -= spendAmount
            
            if random.uniform(0,1) > self.strategy:
                self.stratA(spendAmount,graph)
            else:
                self.stratB(spendAmount,graph)
    
    def stratA(self, amount, graph):
        for consumer in graph.consumers:
            weight = graph.get_edge_weight(consumer,self)
            currentPref = consumer.prefs[self.genre]
            # needs more fine tuning
            newWeight = max(math.tanh(math.log(amount)*(currentPref+1)*weight),0)
            graph.update_edge_weight(consumer,self,newWeight)
    
    def stratB(self,amount,graph):
        for consumer in graph.consumers:
            currentPref = consumer.prefs[self.genre]
            # then calulation with math.log(amount)  

            effectivness = math.tanh(math.log(amount)*(currentPref))
            # Some function that approaches 1 using effectivness
            consumer.modifyPreference(self.genre, effectivness)

    
    def addContribution(self, contributor, contribution):
        if not contributor.id in self.contributors.keys():
            self.contributors[contributor.id] = 0
        # Add to this contributor's total contribution
        self.contributors[contributor.id] += contribution
        self.curr_funds += contribution

    def getContributions(self, contributor):
        if not self.contributors.__contains__(contributor.id):
            return 0
        return self.contributors[contributor.id]

    def getId(self):
        return f"Producer_{self.id}"
    
    def getMarketAverage(self):
        return np.average(self.averageMarketPrefrence)