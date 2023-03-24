class Simulation:
    
    def __init__(self,connectionGraph):
        self.connectionGraph = connectionGraph
        self.totalSteps = 0
        
    def runTimeStep(self):
        self.consumerInteract()
        self.consumerBuy()
        self.producerAdvertise()
        self.upKeep()
        self.totalSteps+=1
        
    def consumerInteract(self):
        for consumer in self.connectionGraph.consumers:
            consumer.notifyNeighbors() #some way to clone so modifications don't carry over in one update
    
    def consumerBuy(self):
        for consumer in self.connectionGraph.consumers:
            for producer in consumer.awareness:
                val = consumer.speculativeValue(producer)
                if val > 0:
                    consumer.buy(producer) #some way to make it so the consumer dosen't keep buying form the same producer
    
    def producerAdvertise(self):
        for producer in self.connectionGraph.producers:
            producer.advertise()
            
    def upKeep(): #some sort of step that can add producers or check to see if produceres should be removed
        pass 
        