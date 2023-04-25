from dataVisualize import Visualizer 
import math
import random

class Simulation:
    def __init__(self, connectionGraph,steps):
        self.steps = steps
        self.connectionGraph = connectionGraph
        self.totalSteps = 0
        self.visualizer = Visualizer(self.connectionGraph.consumers, self.connectionGraph.producers)
        
    def runTimeStep(self):
        # TODO: save data for each timestep
        self.consumerBuy()
        self.producerAdvertise()
        self.consumerUpdate()
        self.visualizer.update(self.connectionGraph.consumers, self.connectionGraph.producers)
        return self.upKeep()
    
    def consumerBuy(self):
        for consumer in self.connectionGraph.consumers:
            for producer in self.connectionGraph.producers:
                val = consumer.speculativeValue(producer)
                if val > 0:
                    consumer.buy(producer)
         
    def consumerUpdate(self):
        for producer in self.connectionGraph.producers:
                for consumer in self.connectionGraph.consumers:
                    producerConsumerWeight = self.connectionGraph.get_edge_weight(producer,consumer)
                    if producerConsumerWeight > 0:
                        for n in consumer.neighbors:
                            currentPref = n.prefs[producer.genre]
                            newWeight = currentPref*producerConsumerWeight*self.connectionGraph.get_edge_weight(n,consumer)
                            self.connectionGraph.update_edge_weight(producer, n, newWeight)
                
    def producerAdvertise(self):
        for producer in self.connectionGraph.producers:
            # Get market analysis value
            trueSentiment = 0
            totalConsumers = 0
            for consumer in self.connectionGraph.consumers:
                totalConsumers += 1
                trueSentiment += consumer.prefs[producer.genre]
            trueSentiment = trueSentiment / totalConsumers
            estimatedAnalysis = random.uniform(trueSentiment-(trueSentiment*1.5), trueSentiment+(trueSentiment*1.5))
            producer.advertise(self.connectionGraph, estimatedAnalysis)
       
    def upKeep(self):
        if self.steps < self.totalSteps:
            self.visualizer.visualize()
            return True
        else:
            self.totalSteps+=1
            return False
        
    def addConFunds(self, maxConsumerFunds):
        for consumer in self.connectionGraph.consumers:
            consumer.curr_funds = random.uniform(.5, 1) * maxConsumerFunds


    def addProGoals(self, maxProducerGoal):
            for producer in self.connectionGraph.producers:
                producer.curr_funds = random.uniform(.5, 1) * maxProducerGoal

