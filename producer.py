import random
import math

class Producer:
   
    def __init__(self, id, goal, genre, strategy,spendPrecentage):
        self.id = id
        self.curr_funds = 0
        self.total_ad_spending = 0
        self.campaign_goal = goal
        self.genre = genre
        self.contributors = dict()
        self.strategy = strategy
        self.spendPrecentage = spendPrecentage

    def advertise(self, graph, marketAnalysis):
        if self.campaign_goal <= self.curr_funds:
            spendAmount = 0
        else:
            spendAmount = self.curr_funds/self.campaign_goal * self.spendPrecentage
        
        self.total_ad_spending += spendAmount 
        
        if random.uniform(0,1) > self.strategy and spendAmount > 0:
            self.stratA(spendAmount,graph)
        else:
            self.stratB(spendAmount,graph)
    
    def stratA(self, amount, graph):
        for consumer in graph.consumers:
            weight = graph.get_edge_weight(consumer,self)
            currentPref = consumer.prefs[self.genre]
            # needs more fine tuning
            newWeight = max(0,min(math.log(amount)*currentPref*weight,1))
            graph.update_edge_weight(consumer,self,newWeight)
    
    def stratB(self,amount,graph):
        for consumer in graph.consumers:
            weight = 0 # connection to influencer
            currentPref = consumer.prefs[self.genre]
            # then calulation with math.log(amount)        

    
    def addContribution(self, contributor, contribution):
        if not self.contributors.keys().__contains__(contributor):
            self.contributors[contributor] = 0
        # Add to this contributor's total contribution
        self.contributors[contributor] += contribution
        self.curr_funds += contribution

    def getContributions(self, contributor):
        if not self.contributors.__contains__(contributor):
            return 0
        return self.contributors[contributor]

    def getId(self):
        return f"Producer_{self.id}"
