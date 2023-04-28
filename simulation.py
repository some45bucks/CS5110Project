from genre import Genre
import random

class Simulation:
    def __init__(self, connectionGraph,steps):
        self.steps = steps
        self.connectionGraph = connectionGraph
        self.totalSteps = 0
        self.marketTrack = []
        
    def runTimeStep(self):
        self.consumerBuy()
        self.producerAdvertise()
        self.consumerUpdate()
        return self.upKeep()
    
    def consumerBuy(self):
        for consumer in self.connectionGraph.consumers:
            for producer in self.connectionGraph.producers:
                val = consumer.speculativeValue(producer)
                if val > 0:
                    consumer.buy(producer)
         
    def consumerUpdate(self):
        for consumer in self.connectionGraph.consumers:
            neighborAverage = [0 for _ in range(len(Genre))]
            for n in consumer.neighbors:
                for i in Genre:
                    neighborAverage[i.value] += self.connectionGraph.consumers[n].prefs[i]/len(consumer.neighbors)

            for i in Genre:
                consumer.prefs[i] += .1*(neighborAverage[i.value])
                consumer.prefs[i] = max(-1,min(1,consumer.prefs[i]))
                
                
    def producerAdvertise(self):
        trueSentiment = [0 for i in range(len(Genre))]
        
        for g in Genre:
            for consumer in self.connectionGraph.consumers:
                trueSentiment[g.value] += consumer.prefs[g]
            trueSentiment[g.value] /= len(self.connectionGraph.consumers)
        
        self.marketTrack = trueSentiment
        
        for producer in self.connectionGraph.producers:
            producer.advertise(self.connectionGraph, trueSentiment[producer.genre.value],self.totalSteps)
       
    def upKeep(self):
        self.totalSteps+=1
        if self.steps <= self.totalSteps:
            return True,self.connectionGraph.producers,self.marketTrack,(self.totalSteps-1)
        else:
            
            return False,self.connectionGraph.producers,self.marketTrack,(self.totalSteps-1)
        
    def addConFunds(self, maxConsumerFunds):
        for consumer in self.connectionGraph.consumers:
            consumer.curr_funds = random.uniform(.5, 1) * maxConsumerFunds


    def addProGoals(self, maxProducerGoal):
            for producer in self.connectionGraph.producers:
                producer.campaign_goal = random.uniform(.5, 1) * maxProducerGoal
                producer.advertiseBudget = producer.campaign_goal * random.uniform(0.01,0.2)

