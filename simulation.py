from dataVisualize import Visualizer 
import math

class Simulation:
    def __init__(self, connectionGraph,steps):
        self.steps = steps
        self.connectionGraph = connectionGraph
        self.totalSteps = 0
        self.visualizer = Visualizer(self.connectionGraph.consumers, self.connectionGraph.producers)
        
    def runTimeStep(self):
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
    
    #make prefrences play a role in consumer updates
    #some more sophisticated udate method                
    def consumerUpdate(self):
        for producer in self.connectionGraph.producers:
                for consumer in self.connectionGraph.consumers:
                    producerConsumerWeight = self.connectionGraph.get_edge_weight(producer,consumer)
                    if producerConsumerWeight > 0:
                        for n in consumer.neighbors:
                            newWeight = producerConsumerWeight*self.connectionGraph.get_edge_weight(n,consumer)
                            self.connectionGraph.update_edge_weight(producer, n, newWeight)
                
    #producer advertise needs to affect awarenss and prefrence
    def producerAdvertise(self):
        for producer in self.connectionGraph.producers:
            amount = producer.advertise()
            for consumer in self.connectionGraph.consumers:
                weight = self.connectionGraph.get_edge_weight(consumer,producer)
                currentPref = consumer.prefs[producer.genre]
                consumer.modifyPreference(producer.genre,2/(1+math.e**(-(weight*amount + currentPref))) - 1)
       
    def upKeep(self):
        if self.steps < self.totalSteps:
            self.visualizer.visualize()
            return True
        else:
            self.totalSteps+=1
            return False
        
        