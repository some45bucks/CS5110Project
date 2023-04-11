from dataVisualize import Visualizer 
import math

class Simulation:
    def __init__(self, connectionGraph,steps):
        self.steps = steps
        self.currentStep = 0
        self.connectionGraph = connectionGraph
        self.totalSteps = 0
        self.visualizer = Visualizer(self.connectionGraph.consumers, self.connectionGraph.producers)
        
    def runTimeStep(self):
        self.totalSteps += 1
        self.consumerBuy()
        self.producerAdvertise()
        self.visualizer.update(self.connectionGraph.consumers, self.connectionGraph.producers)
        return self.upKeep()
    
    def consumerBuy(self):
        for consumer in self.connectionGraph.consumers:
            for producer in self.connectionGraph.consumerAwareness(consumer):
                val = consumer.speculativeValue(producer)
                if val > 0:
                    consumer.buy(producer)
                    
    def consumerUpdate(self):
        for producer in self.connectionGraph.producers:
                for consumer in self.connectionGraph.consumers:
                    producerConsumerWeight = self.connectionGraph.get_edge_weight(producer,consumer)
                    if producerConsumerWeight > 0:
                        for n in consumer.neighbors:
                            newWeight = producerConsumerWeight*self.connectionGraph.get_edge_weight(n,consumer)
                            self.connectionGraph.update_edge_weight(producer, n, newWeight)
                
    
    def producerAdvertise(self):
        for producer in self.connectionGraph.producers:
            amount = producer.advertise()
            for consumer in self.connectionGraph.consumers:
                weight = self.connectionGraph.get_edge_weight(consumer,producer)
                consumer.modifyPreference(producer.genre,2/(1+math.e**(-weight*amount)) + 1)
       
    def upKeep(self):
        if self.steps < self.currentStep:
            self.visualizer.visualize()
            return True
        else:
            self.currentStep+=1
            return False
        
        