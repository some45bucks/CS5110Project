import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, consumers, producers):
        self.consumer_data = {}
        self.producer_data = {}
        for consumer in consumers:
            self.consumer_data[consumer.id] = {'current_funds': [consumer.curr_funds]}
        for producer in producers:
            self.producer_data[producer.id] = {'current_funds': [producer.curr_funds]}
    
    def update(self, consumers, producers):
        for consumer in consumers:
            self.consumer_data[consumer.id]['current_funds'].append(consumer.curr_funds)
        for producer in producers:
            self.producer_data[producer.id]['current_funds'].append(producer.curr_funds)
            
    def visualize(self):
        for consumer_id, data in self.consumer_data.items():
            plt.plot(data['current_funds'], label=f'Consumer {consumer_id}')
        for producer_id, data in self.producer_data.items():
            plt.plot(data['current_funds'], label=f'Producer {producer_id}')
        plt.legend()
        plt.show()