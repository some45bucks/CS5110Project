from dataVisualize import Visualizer 
import math

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
            producer.advertise(self.connectionGraph)
       
    def upKeep(self):
        if self.steps < self.totalSteps:
            self.visualizer.visualize()
            return True
        else:
            self.totalSteps+=1
            return False
