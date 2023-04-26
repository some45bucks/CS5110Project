import matplotlib.pyplot as plt
from genre import Genre

class Visualizer:
    
    colorMap = ['red','blue','green','yellow','purple','orange']
       
    def __init__(self, consumers, producers):
        self.consumer_data = {}
        self.producer_data = {}
        self.marketPrefs = {}
        
        for g in Genre:
            self.marketPrefs[g] = []
        
        for consumer in consumers:
            self.consumer_data[consumer.id] = {'current_funds': []}
        for producer in producers:
            self.producer_data[producer.id] = {'current_funds': [],'g':producer.genre}
    
    def update(self, consumers, producers, marketPrefs):
        for g in Genre:
            self.marketPrefs[g].append(marketPrefs[g.value])
        for consumer in consumers:
            self.consumer_data[consumer.id]['current_funds'].append(consumer.curr_funds)
        for producer in producers:
            self.producer_data[producer.id]['current_funds'].append(producer.curr_funds)
            
    def visualize(self):
        plt.figure()
        for genre_id, data in self.marketPrefs.items():
            plt.plot(data,label=f"{genre_id.name}",color=self.colorMap[genre_id.value])
        
        plt.legend()    
        
        plt.figure()
        for consumer_id, data in self.consumer_data.items():
            plt.plot(data['current_funds'],linestyle='dashed')
            
        plt.figure()
        for producer_id, data in self.producer_data.items():
            plt.plot(data['current_funds'],color=self.colorMap[data['g'].value])
            
        plt.show()